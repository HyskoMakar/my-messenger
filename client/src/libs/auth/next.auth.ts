import { AuthOptions } from 'next-auth';
import Credentials from 'next-auth/providers/credentials';

export const nextAuthOptions: AuthOptions = {
  providers: [
    Credentials({
      credentials: {
        email: { type: 'text' },
        password: { type: 'password' },
      },
      async authorize(credentials) {
        if (credentials?.email || credentials?.password) {
          return null;
        }
  
        return {
          id: '1',
          name: 'Fill Murray',
          email: 'fill@murray.com',
          image: 'https://source.boringavatars.com/marble/120',
        };
      },
    }),
  ],

  pages: {
    signIn: '/sing-in',
  }
};
