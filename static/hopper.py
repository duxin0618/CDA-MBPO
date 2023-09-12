import numpy as np

class StaticFns:

    @staticmethod
    def termination_fn(obs, act, next_obs):
        assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2

        height = next_obs[:, 0]
        angle = next_obs[:, 1]
        not_done =  np.isfinite(next_obs).all(axis=-1) \
                    * np.abs(next_obs[:,1:] < 100).all(axis=-1) \
                    * (height > .7) \
                    * (np.abs(angle) < .2)

        done = ~not_done
        done = done[:,None]
        return done

    @staticmethod
    def reward_fn(obs, act, next_obs):
        reward_ctrl = -0.1 * np.sum(np.square(act), axis=1)
        reward_run = obs[:, 5]
        reward_height = -3.0 * np.square(obs[:, 0] - 1.3)
        reward = reward_run + reward_ctrl + reward_height + 1.0
        return reward
