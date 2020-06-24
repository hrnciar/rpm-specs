Name:       nnn
Version:    3.2
Release:    1%{?dist}
Summary:    The missing terminal file browser for X

License:    BSD
URL:        https://github.com/jarun/nnn
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  readline-devel

%description
nnn is probably the fastest and most resource-sensitive (with all
its capabilities) file browser you have ever used. It's extremely flexible
too - integrates with your DE and favourite GUI utilities, works with
the desktop opener, supports bookmarks, has smart navigation shortcuts,
navigate-as-you-type mode, disk usage analyzer mode, comprehensive file
details and much more. nnn was initially forked from noice but is
significantly different today.

Cool things you can do with nnn:

 - open any file in the default desktop application or a custom one
 - navigate-as-you-type (search-as-you-type enabled even on directory switch)
 - check disk usage with number of files in current directory tree
 - run desktop search utility (gnome-search-tool or catfish) in any directory
 - copy absolute file paths to clipboard, spawn a terminal and use the paths
 - navigate instantly using shortcuts like ~, -, & or handy bookmarks
 - use cd ..... at chdir prompt to go to a parent directory
 - detailed file stats, media info, list and extract archives
 - pin a directory you may need to revisit and jump to it anytime
 - lock the current terminal after a specified idle time
 - change directory on exit

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i "s|^install: all|install:|" Makefile

%build
%set_build_flags
%make_build STRIP=/bin/true

%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  misc/auto-completion/bash/nnn-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  misc/auto-completion/fish/nnn.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  misc/auto-completion/zsh/_nnn

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nnn-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/nnn.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_nnn

%changelog
* Thu Jun 18 22:46:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.2-1
- Update to 3.2 (#1823267)

* Mon Feb 17 02:14:43 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0-1
- Update to 3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 16:32:00 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.9-1
- Release 2.9 (#1791235)

* Thu Dec 05 18:01:02 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.8.1-1
- Release 2.8.1

* Mon Oct 07 16:12:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.7-1
- Release 2.7

* Thu Aug 08 20:47:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.6-1
- Release 2.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 21:29:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.5-1
- Release 2.5

* Mon Mar 18 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.4-1
- Release 2.4

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.3-1
- Release 2.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.2-1
- Release 2.2

* Fri Nov 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1-1
- Release 2.1

* Fri Oct 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0-1
- Release 2.0

* Fri Aug 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.9-1
- Release 1.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.8-1
- Release 1.8

* Thu Mar 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.7-1
- Release 1.7

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6-1
- First RPM release
