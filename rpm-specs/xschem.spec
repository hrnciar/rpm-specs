# xschem Package description for Fedora/Free Electronic Lab
#
%global rpm_has_recommends    %(rpm --version | awk -e '{print ($3 > 4.12)}')
#
Name:           xschem
Version:        2.9.2
Release:        4%{?dist}
Summary:        Schematic capture and Netlisting EDA tool

License:        GPLv2+
URL:            http://repo.hu/projects/xschem
Source0:        http://repo.hu/projects/xschem/releases/xschem-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gawk
BuildRequires:  flex, bison
#BuildRequires:  flex-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(cairo-xcb)
#BuildRequires:  cairo-devel
#BuildRequires:  xcb-util-devel

%if %rpm_has_recommends
Recommends:     %{name}-doc = %{version}-%{release}
%endif

#Requires:   tcl, tk


%description
%{name} is a schematic capture program, it allows creation of hierarchical
representation of circuits with a top down approach. By focusing on
interfaces, hierarchy and instance properties, a complex system can be
described in terms of simpler building blocks. A VHDL or Verilog or Spice
netlist can be generated from the drawn schematic, allowing the simulation
of the circuit. Key feature of the program is its drawing engine written in C
and using directly the Xlib drawing primitives; this gives very good
speed performance, even on very big circuits. The user interface is
built with the Tcl-Tk toolkit, Tcl is also the extension language used.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.


%prep
%autosetup


%build
./"configure" --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} --symbols
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS Changelog LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/xschem.1*


%files doc
%{_docdir}/%{name}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.9.2-1
- Upstream new release

* Sun Jul 14 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.9.0-1
- Upstream new release

* Sun Feb 17 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.8.2-2
- apply suggestions from package reviewers

* Sun Jan 27 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.8.2-1
- Upstream new release

* Sun Dec 02 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.8.1-1
- Upstream new release

* Tue Nov 06 2018 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.8.0-1
- Initial proposal
