// test/VulnSqlJdbc.java
import java.sql.*;
import javax.servlet.http.*;

public class VulnSqlJdbc extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    String id = req.getParameter("id");
    try (Connection c = DriverManager.getConnection("jdbc:sqlite:db")) {
      // Vulnerable: concatenated SQL using user input
      Statement s = c.createStatement();
      ResultSet r = s.executeQuery("SELECT * FROM orders WHERE id = " + id);
      // ...
    } catch (Exception e) {}
  }
}
