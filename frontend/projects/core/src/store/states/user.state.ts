export interface IUserState {
    id: number;
    username: string;
    gender: string;
    birthday: string;
    main_photo: string;
}

export class UserState implements IUserState {
    constructor(
        public id: number = 0,
        public username: string = 'undefined',
        public gender: string = 'undefined',
        public birthday: string = 'undefined',
        public main_photo: string = 'undefined'
        ) {


    }
}