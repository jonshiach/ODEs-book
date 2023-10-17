% Euler method solution to an initial value problem

% Define ODE function
f = @(t, y) t * y;

% Define IVP parameters
tspan = [0, 1];     % boundaries of the t domain
y0 = 1;             % initial values
h = 0.2;            % step length

% Calculate the solution to the IVP
[t, y] = solveIVP(f, tspan, y0, h, @euler);

% Print table of solution values
fprintf("|  t   |     y     |\n|:----:|:---------:|");
for n = 1 : length(t)
    fprintf("\n| %4.2f | %9.6f | %9.6f | %8.2e |", t(n), y(n));
end
fprintf("\n")

% Plot solution
plot(t, y, "b-o", LineWidth=2, MarkerFaceColor="b")
axis padded
xlabel("$t$", FontSize=14, Interpreter="latex")
ylabel("$y$", FontSize=14, Interpreter="latex")
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
function ynew = euler(f, t, y, h)

ynew = y + h * f(t, y);

end