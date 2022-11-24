// function add_age() {
//     eel.add_ages(vm.$data.age, 10086)
// }
//
// eel.expose(set_age)
// function set_age(d) {
//     vm.$data.age = d
// }
// eel.expose(py_login)
function py_login(u,p){
    eel.py_login(u,p)
}

eel.expose(py_login_response)
function py_login_response(msg){
    vm.$data.loginsuc = false
    vm.$data.loginerr = false
    if(msg === "200"){
        vm.$data.loginsuc = true
        vm.$data.is_login = true
    }else{
        vm.$data.loginerr = true
    }
}