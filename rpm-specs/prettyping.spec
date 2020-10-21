Name: prettyping
Version: 1.0.1
Release: 6%{?dist}
Summary: Compact, colorful ping tool for your terminal
License: MIT

URL: http://denilson.sa.nom.br/prettyping
Source0: https://github.com/denilsonsa/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: bash coreutils gawk iputils
BuildArch: noarch

%description
prettyping runs the standard ping in background and parses its output,
showing ping responses in a graphical way at the terminal, by using colors
and Unicode characters.

Don’t have support for UTF-8 in your terminal?
No problem, you can disable it and use standard ASCII characters instead.

Don’t have support for colors?
No problem, you can also disable them.


%prep
%setup -q
sed -e 's|#!/usr/bin/env bash|#!/usr/bin/bash|' -i ./%{name}


%build
# Nothing to do here


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 ./%{name}  %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 5 2018 Artur Iwicki <fedora@svgames.pl> - 1.0.1-1
- Initial packaging
