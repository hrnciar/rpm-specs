Name:           herbstluftwm
Version:        0.7.2
Release:        3%{?dist}
Summary:        A manual tiling window manager
License:        BSD
URL:            http://herbstluftwm.org
Source0:        http://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.
Its main features can be described with:

- The layout is based on splitting frames into subframes which can be split
again or can be filled with windows;
- Tags (or workspaces or virtual desktops or …) can be added/removed at
runtime. Each tag contains an own layout exactly one tag is viewed on each
monitor. The tags are monitor independent;
- It is configured at runtime via ipc calls from herbstclient. So the
configuration file is just a script which is run on startup.

%package        zsh
Summary:        Herbstluftwm zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh

%description    zsh
This package provides zsh completion script of %{name}.

%package        fish
Summary:        Herbstluftwm fish completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish

%description    fish
This package provides fish completion script of %{name}.

%prep
%autosetup

%build
# Set the proper build flags
%set_build_flags
%make_build VERBOSE=""

%install
%make_install ZSHCOMPLETIONDIR='%{_datadir}/zsh/site-functions' \
              FISHCOMPLETIONDIR='%{_datadir}/fish/vendor_completions.d' \
              BASHCOMPLETIONDIR='%{_datadir}/bash-completion/completions' \
              PREFIX='%{_prefix}'

# Change the shebangs of the upstream files to be proper
for f in "%{buildroot}%{_pkgdocdir}/examples/*.sh"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

for f in "%{buildroot}%{_sysconfdir}/xdg/%{name}/*"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" "%{buildroot}%{_bindir}/dmenu_run_hlwm"

# Remove unnecessary and/or redundant files
rm %{buildroot}%{_pkgdocdir}/INSTALL
rm %{buildroot}%{_pkgdocdir}/LICENSE

mv %{buildroot}%{_datadir}/bash-completion/completions/herbstclient-completion \
   %{buildroot}%{_datadir}/bash-completion/completions/herbstclient

%files
%license LICENSE
%doc AUTHORS BUGS MIGRATION NEWS
%doc doc/*.{html,txt}
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_pkgdocdir}/examples/

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%files fish
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Jani Juhani Sinervo <jani@sinervo.fi> - 0.7.2-1
- Revive under new maintainer

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Christopher Meng <rpm@cicku.me> - 0.6.2-1
- Update to 0.6.2

* Tue Mar 25 2014 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Fri Mar 21 2014 Christopher Meng <rpm@cicku.me> - 0.6.0-1
- Update to 0.6.0

* Fri Dec 27 2013 Christopher Meng <rpm@cicku.me> - 0.5.3-1
- Update to 0.5.3

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-2
- Move bash completion to better place.

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-1
- Initial Package.
