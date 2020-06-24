%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

%global shortname tclnagios

Name:           tcl-tclnagios
Version:        1.3
Release:        9%{?dist}
Summary:        Library to assist with writing Nagios plugins in Tcl

License:        LGPLv2
URL:            https://github.com/gitwart/%{shortname}
Source0:        https://github.com/gitwart/%{shortname}/archive/v%{version}/%{shortname}-%{version}.tar.gz

Provides:       tclnagios = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  tcl-devel
Requires:       tcllib

%description
A set of library functions to make it easier to write Nagios plugins in Tcl.


%prep
%autosetup -n %{shortname}-%{version}
chmod a-x examples/*

%build
%configure --datadir=%{tcl_sitelib}
%make_build

%install
%make_install


%files
%doc examples/
%license COPYING
%{tcl_sitelib}/%{shortname}%{version}



%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 9 2017 Michael Thomas <wart@kobold.org> 1.3-4
- spec file cleanup

* Tue Aug 8 2017 Michael Thomas <wart@kobold.org> 1.3-3
- Include license file, example code

* Tue Aug 8 2017 Michael Thomas <wart@kobold.org> 1.3-2
- Change define to global

* Mon Aug 7 2017 Michael Thomas <wart@kobold.org> 1.3-1
- Bump version after moving project to github

* Mon Jan 11 2016 Michael Thomas <thomas@hep.caltech.edu> 1.2-2
- Fix boundary condition logic for comparing values to a range

* Wed Aug 17 2011 Michael Thomas <thomas@hep.caltech.edu> 1.2-1
- Added utility function for comparing numeric values to a range

* Fri Sep 24 2010 Michael Thomas <thomas@hep.caltech.edu> 1.1-2.3
- Bump release to test koji builds

* Thu Sep 9 2010 Michael Thomas <thomas@hep.caltech.edu> 1.1-2.2
- Bump release to test koji builds

* Wed Sep 8 2010 Michael Thomas <thomas@hep.caltech.edu> 1.1-2.1
- Bump release to test koji builds

* Mon Apr 13 2009 Michael Thomas <thomas@hep.caltech.edu> 1.1-2
- Bump release to ensure that clients have the latest version.

* Thu Jul 10 2008 Michael Thomas <thomas@hep.caltech.edu> 1.1-1
- Support for publishing passive results via send_nsca
- Better command line processing

* Sun Sep 9 2007 Michael Thomas <thomas@hep.caltech.edu> 1.0-1
- Initial package
