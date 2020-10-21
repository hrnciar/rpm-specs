%global pkg flycheck-pycheckers

Name:           emacs-%{pkg}
Version:        0.15
Release:        1%{?dist}
Summary:        Multiple syntax checker for Python in Emacs, using Flycheck

License:        GPLv3+
URL:            https://github.com/msherry/%{pkg}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-flycheck
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-flycheck
BuildArch:      noarch

%description
This package provides a way to run multiple syntax checkers on Python code, in
parallel. The list of supported checkers includes:
* pylint
* flake8
* pep8
* pyflakes
* mypy
* bandit
This is an alternative way of running multiple Python syntax checkers in
Flycheck that doesn't depend on Flycheck's chaining mechanism.

Flycheck is opinionated about what checkers should be run, and chaining is
difficult to get right. This package assumes that the user knows what they want,
and can configure their checkers accordingly — if they want to run both flake8
and pylint, that's fine.

This also allows us to run multiple syntax checkers in parallel, rather than
sequentially.


%prep
%autosetup -n %{pkg}-%{version} -p0

# Fix shebang
sed -e 's|^#!.*|#!%{__python3}|' bin/pycheckers.py >bin/pycheckers.py.new && \
touch -r bin/pycheckers.py bin/pycheckers.py.new && \
mv bin/pycheckers.py.new bin/pycheckers.py


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a bin/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
chmod 0755  $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/bin/pycheckers.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc pycheckers-EXAMPLE README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.15-1
- Initial RPM release
