Name:           hstr
Version:        2.2
Release:        3%{?dist}
Summary:        Suggest box like shell history completion

License:        ASL 2.0
URL:            https://github.com/dvorka/hstr
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
A command line utility that brings improved shell command completion
from the history. It aims to make completion easier and faster than Ctrl-r.


%prep
%autosetup
autoreconf -fiv

%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc Changelog README.md
%{_bindir}/hh
%{_bindir}/%{name}
%{_datadir}/bash-completion/
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Leigh Scott <leigh123linux@gmail.com> - 2.2-1
- Update to 2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.22-8
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 1.22-1
- Update to 1.22
- Remove build requires on autoconf

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.21-4
- Rebuild for readline 7.x

* Sat Nov 12 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-3
- Remove requires on ncurses and readline

* Thu Oct 27 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-2
- Add build requires on autoconf

* Sat Oct 22 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.21-1
- Update to 1.21
- Change source URL to GitHub
- Add build requires on automake
- Use %%autosetup macro

* Fri Jan 22 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 1.19-1
- Initial RPM release
