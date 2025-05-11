import { useQuery } from '@tanstack/react-query';
import request  from './utils/api';
import { IUser } from './interfaces/IUSer';
import { viewport, initData, init } from '@telegram-apps/sdk';

init();
viewport.mount();

initData.restore();
viewport.expand();

const App = () => {
  const {data: user, isLoading} = useQuery({
    queryKey: ['user'],
    queryFn: async () => {
      return (await request('users/get')).data;
    },
    select: (data) => data.user as IUser
  })

  return (
    <>
      {isLoading ? (
        <div className="flex justify-center items-center h-screen">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500"></div>
        </div>
      ): (
        <>{user?.name}</>
      )}
    </>
  );
}

export default App;