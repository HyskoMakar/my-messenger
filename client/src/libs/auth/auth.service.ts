import { $fetch } from '@/$api/api.fetch';
import { SignUpForm, User } from './models';

class AuthService {
  public async signUp(data: SignUpForm): Promise<User> {
    return $fetch.post<User>('/sign-up', data);
  }
}

export const authService = new AuthService();
