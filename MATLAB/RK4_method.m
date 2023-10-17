% RK4 method solution to an initial value problem

% Define ODE function
f = @(t, y) t * y;

% Define exact solution
exact = @(t) exp(t .^ 2 / 2);

% Define IVP parameters
tspan = [0, 1];     % boundaries of the t domain
y0 = 1;             % initial values
h = 0.2;            % step length

% Calculate the solution to the IVP
[t, yEuler] = solveIVP(f, tspan, y0, h, @euler);
[t, yRK4] = solveIVP(f, tspan, y0, h, @rk4);

% Print table of solution values
fprintf("\n|  t   |   Euler   |    RK4    |   Exact   |\n|:----:|:---------:|:---------:|:---------:|");
for n = 1 : length(t)
    fprintf("\n| %4.2f | %9.6f | %9.6f | %9.6f | %9.6f |", t(n), yEuler(n), yRK4(n), exact(t(n)));
end
fprintf("\n")

% Plot solution
tExact = linspace(tspan(1), tspan(2), 200);
plot(tExact, exact(tExact), "k-", LineWidth=2)
hold on
plot(t, yEuler, "b-o", LineWidth=2, MarkerFaceColor="b")
plot(t, yRK4, "r-o", LineWidth=2, MarkerFaceColor="r")
hold off
axis padded
xlabel("$t$", FontSize=14, Interpreter="latex")
ylabel("$y$", FontSize=14, Interpreter="latex")
legend("Exact", "Euler", "RK4", Location="north west")
shg

% ----------------------------------------------------------------------
function [t, y] = solveIVP(f, tspan, y0, h, solver)

% Define t and y arrays
t = (tspan(1) : h : tspan(2));
y = zeros(length(t), length(y0));
y(1,:) = y0;

% Loop through the steps and calculate single step solver solution
for n = 1 : length(t) - 1
    y(n+1,:) = solver(f, t(n), y(n,:), h);
end

end

% ----------------------------------------------------------------------
function ynew = rk4(f, t, y, h)

k1 = f(t, y);
k2 = f(t + 0.5 * h, y + 0.5 * h * k1);
k3 = f(t + 0.5 * h, y + 0.5 * h * k2);
k4 = f(t + h, y + h * k3);
ynew = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4);

end

% ----------------------------------------------------------------------
function ynew = euler(f, t, y, h)

ynew = y + h * f(t, y);

end