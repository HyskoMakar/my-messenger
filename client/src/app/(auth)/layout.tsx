import { Flex } from '@chakra-ui/react';

export default function AuthLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <Flex
      as='main'
      minH='100vh'
      alignItems='center'
      justifyContent='center'>
      {children}
    </Flex>
  );
}
