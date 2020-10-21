Name: profile-cleaner
Version: 2.41
Release: 2%{?dist}
Summary: Script to vacuum and reindex sqlite databases used by Firefox and by Chrome
BuildArch: noarch

License: MIT
URL: https://github.com/graysky2/profile-cleaner
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: bc
Requires: findutils
Requires: parallel
Requires: sqlite

%description
Use profile-cleaner to reduce the size of browser profiles by organizing their
sqlite databases using sqlite3's vacuum and reindex functions. The term
"browser" is used loosely since profile-cleaner happily works on some email
clients and newsreaders too.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/pc
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_pc
%{_mandir}/man1/*.1*


%changelog
* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.41-2
- build: minor fix per review rh#1885718

* Tue Oct  6 22:25:28 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.41-1
- Initial package
