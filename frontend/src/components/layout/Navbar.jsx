
const Navbar = () => {
    const handleLayout = () =>{
        localStorage.removeItem("token");
        window.location.href("/login");
    }

return (
    <nav className="navbar">
        <h2 className="navbar-title">BunkMaster</h2>
        <button className="navbar-layout" onClick={handleLayout} > Logout </button>
    </nav>
)   

};

export default Navbar;