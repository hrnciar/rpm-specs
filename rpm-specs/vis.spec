Name:           vis
Version:        0.6
Release:        1%{?dist}
Summary:        A vim-like editor with structural regex from plan9

# The entire source code is ISC except for the following exceptions,
# that are also found in the LICENSE-file of the project:
# ./configure is MIT licensed
# map.c and map.h are under CC0
# libutf.c and libutf.h are MIT licensed
# sam.c and sam.h are under a ISC-like license
# All files under lua/lexers/ are MIT licensed
License:        ISC and MIT and CC0
URL:            https://github.com/martanne/%{name}/
Source0:        https://github.com/martanne/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(tre)
BuildRequires:  pkgconfig(lua) >= 5.2
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig(libselinux)
Requires:       lua-lpeg >= 0.12

%description
A Vim-like editor with structural regular expressions
inspired by Plan9's Sam-editor.

%package doc
Summary:        Docs for the Lua API of Vis
BuildRequires:  lua-ldoc
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}

%prep
%autosetup -n vis-%{version}

%build
%configure
%make_build

# create Lua API docs
%make_build luadoc-all

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/vis
%{_bindir}/vis-clipboard
%{_bindir}/vis-complete
%{_bindir}/vis-digraph
%{_bindir}/vis-menu
%{_bindir}/vis-open
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1.*
%exclude %{_pkgdocdir}/LICENSE

%files doc
%doc lua/doc/index.html lua/doc/ldoc_fixed.css

%changelog
* Mon Jun 15 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 0.6-1
- Update to 0.6

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 07 2018 Jani Juhani Sinervo <jani@sinervo.fi> - 0.5-1
- Initial attempt at official inclusion
