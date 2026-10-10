class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            if loser not in losses:
                losses[loser] = 0
            # only the loser gets plus 1
            losses[loser] += 1
        
        zero_losses = []
        one_loss = []

        for player in losses:
            # never lost
            if losses[player] == 0:
                zero_losses.append(player)
            # lost one game
            elif losses[player] == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()
        return [zero_losses, one_loss]


                


