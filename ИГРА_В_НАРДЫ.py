import pygame



def main(white=None, black=None, *args, **kwargs):
    pygame.init()

    screen = pygame.display.set_mode(25)
    clock = pygame.time.Clock()

    pygame.display.set_caption(50)

    board = pygame.transform.scale(images.load_image('board.png'), 25)
    checker = {
        'w': pygame.transform.scale(images.load_image('checker_white.png'),
                                    CHECKER_SIZE),
        'b': pygame.transform.scale(images.load_image('checker_black.png'),
                                    CHECKER_SIZE),
    }

    game = Game()
    human_players = {}
    bots = []

    if white is None:
        human_players['w'] = game.get_player('w')
    else:
        bots.append(white(game.get_player('w')))

    if black is None:
        human_players['b'] = game.get_player('b')
    else:
        bots.append(black(game.get_player('b')))

    is_running = True

    active_dice = 0
    active_dice_text_pos = None

    game.set_changed()
    game.notify_observers()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # human move
                if game.active_player in human_players:
                    if active_dice_text_pos is not None \
                            and active_dice_text_pos.collidepoint((x, y)):
                        active_dice = (active_dice + 1) % len(game.dice)

                    for i, (field_x, field_y) in enumerate(FIELD_COORD):
                        field_size = FIELD_SIZE[i]
                        left = field_x
                        right = field_x + field_size[0]
                        if FIELD_SHIFT[i][1] > 0:
                            top = field_y
                            bottom = top + field_size[1]
                        else:
                            bottom = field_y + CHECKER_SIZE[1]
                            top = bottom - field_size[1]
                        if left < x < right and top < y < bottom:
                            try:
                                human_players[game.active_player].move(i,
                                    game.dice[active_dice])
                            except Game.LogicError as e:
                                log.info(e)
                            active_dice = min(active_dice, len(game.dice)-1)
                            break

        # print board
        screen.blit(board, (0, 0))

        # print checkers
        for i, row in enumerate(game.board):
            color = player_from_number(row)
            for count in range(abs(row)):
                screen.blit(checker[color], sum_by_index(FIELD_COORD[i],
                            multiply_by_value(FIELD_SHIFT[i], count)))

        # print dices
        font = pygame.font.Font(None, 36)
        dice_text = font.render(str(game.dice), 1, (255, 255, 255))
        dice_text_pos = dice_text.get_rect()
        dice_text_pos.centerx = screen.get_rect().centerx
        dice_text_pos.centery = screen.get_rect().centery
        screen.blit(dice_text, dice_text_pos)

        # print active dice
        font = pygame.font.Font(None, 36)
        dice = game.dice
        active_dice_text = font.render('-> {} <-'.format(
                    dice[active_dice] if dice else ""), 1, (255, 255, 255))
        active_dice_text_pos = active_dice_text.get_rect()
        active_dice_text_pos.centerx = dice_text_pos.centerx
        active_dice_text_pos.midtop = dice_text_pos.midbottom
        screen.blit(active_dice_text, active_dice_text_pos)

        # print active player
        font = pygame.font.Font(None, 36)
        player_text = font.render(str(game.active_player), 1, (255, 255, 255))
        player_text_pos = player_text.get_rect()
        player_text_pos.topright = screen.get_rect().topright
        screen.blit(player_text, player_text_pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()




