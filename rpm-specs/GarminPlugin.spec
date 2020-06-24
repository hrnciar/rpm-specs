# Are licenses packaged using %%license?
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
%global with_license 1
%endif # 0%%{?fedora} >= 22 || 0%%{?rhel} >= 8

Name:		GarminPlugin
Version:	0.3.27
Release:	12%{?dist}
Summary:	Garmin Communicator Plugin port for Linux
%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

# ===== License-breakdown =====
#
# GPLv3+
# ------
# * except the files explicitly named below
#
# BSD (3 clause)
# --------------
# src/npapi/npruntime.h
#
# MPLv1.1 and (GPLv2 or LGPLv2)
# -----------------------------
# src/npapi/npapi.h
# src/npapi/npfunctions.h
# src/npapi/nptypes.h
#
License:	BSD and GPLv3+ and (MPLv1.1 and (GPLv2 or LGPLv2))
URL:		http://www.andreas-diesner.de/garminplugin
Source0:	https://github.com/adiesner/%{name}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

BuildRequires:  gcc-c++
BuildRequires:	garmintools-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	tinyxml-devel
BuildRequires:	zlib-devel

Requires:	garmintools%{?_isa}
Requires:	mozilla-filesystem%{?_isa}

%description
This browser plugin has the same methods and properties as the
official Garmin Communicator Plugin.  It can be used to transfer
GPX files (Geocache Descriptions) to your garmin device using
the official Garmin Javascript API.  Its functionality depends
on the device you use:
  * Edge305/Forerunner305: ReadFitnessData, ReadGpsData, No write support
  * Edge705/Oregon/Dakota: ReadFitnessData, ReadGpsData, Write Gpx files
  * Edge800: ReadFitnessData, Write Gpx/Tcx Files
  * Other devices: Executes external command to write Gpx to device


%prep
%setup -q

# Remove unneeded stuff.
%{__rm} -rf build/


%build
pushd src
%configure --without-optflags
%{__make} %{?_smp_mflags}
popd


%install
%if 0%{?rhel} && 0%{?rhel} <= 5
%{__rm} -rf %{buildroot}
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

%{__mkdir} -p %{buildroot}%{_libdir}/mozilla/plugins
%{__install} -pm 0755 src/np%{name}.so			\
	%{buildroot}%{_libdir}/mozilla/plugins

%files
%if 0%{?with_license}
%license COPYING
%else  # 0%%{?with_license}
%doc COPYING
%endif # 0%%{?with_license}
%doc HISTORY README test.html
%{_libdir}/mozilla/plugins/np%{name}.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 30 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.27-2
- added needed stuff for el5

* Mon Jun 29 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.27-1
- new upstream release 0.3.27 (#1236300)
- dropped Patch0: changes are applied in upstream tarball

* Mon Jun 29 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.26-1
- initial import (#1236300)

* Mon Jun 29 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.26-0.4
- updated Patch0: got accepted by upstream and adds full
  license-text besides all previous improvements
- dropped Patch1: obsoleted by updated Patch0

* Sun Jun 28 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.26-0.3
- added license-breakdown to spec-file
- added Patch1: fix `warning: 'mdret' may be used uninitialized
  in this function [-Wmaybe-uninitialized]`

* Sun Jun 28 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.26-0.2
- fixed License-tag
- added Requires: mozilla-filesystem
- informed upstream about missing full license-text and
  added a template for including the file into the package
- added Patch0: adding configure-option to opt-out upstream's
  optimization flags

* Sat Jun 27 2015 Björn Esser <bjoern.esser@gmail.com> - 0.3.26-0.1
- initial rpm-release (#1236300)
