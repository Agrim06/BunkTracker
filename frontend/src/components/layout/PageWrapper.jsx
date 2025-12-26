import Navbar from "./Navbar";

const PageWrapper = ({ children }) => {
  return (
    <>
      <Navbar />
      <main className="page-wrapper">
        {children}
      </main>
    </>
  );
};

export default PageWrapper;
