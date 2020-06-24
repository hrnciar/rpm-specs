Name:           sasutils
Version:        0.3.10
Release:        3%{?dist}
Summary:        Serial Attached SCSI (SAS) utilities

License:        ASL 2.0
URL:            https://github.com/stanford-rc/sasutils
Source0:        https://github.com/stanford-rc/sasutils/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       sg3_utils
Requires:       smp_utils

%{?python_provide:%python_provide python-sasutils}

%description
sasutils is a set of command-line tools and a Python library to ease the
administration of Serial Attached SCSI (SAS) fabrics.

%prep
%setup -q

%build
%py3_build

%install
%py3_install
install -d %{buildroot}/%{_mandir}/man1
install -p -m 0644 doc/man/man1/sas_counters.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_devices.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_discover.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/ses_report.1 %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/sas_counters
%{_bindir}/sas_devices
%{_bindir}/sas_discover
%{_bindir}/sas_mpath_snic_alias
%{_bindir}/sas_sd_snic_alias
%{_bindir}/ses_report
%{python3_sitelib}/sasutils/
%{python3_sitelib}/sasutils-*-py?.?.egg-info
%{_mandir}/man1/sas_counters.1*
%{_mandir}/man1/sas_devices.1*
%{_mandir}/man1/sas_discover.1*
%{_mandir}/man1/ses_report.1*
%doc README.rst
%license LICENSE.txt

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.10-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Stephane Thiell <sthiell@stanford.edu> 0.3.10-1
- update version
- update Source to download from GitHub directly

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.9-1
- update version

* Tue Aug 22 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.8-2
- always remove shebang from Python modules
- removed unwanted Group tag
- removed useless/duplicate Provides tag

* Fri Aug 18 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.8-1
- added man pages

* Wed Aug 16 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.5-1
- packaging improvements

* Tue Jul  4 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.4-1
- build against python3 only
- install LICENSE.txt file
- use python_provide macro and update to follow Fedora packaging guidelines

* Sat May 20 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.3-1
- update version (bug fixes)

* Wed Mar 29 2017 Mikhail Lesin <mlesin@gmail.com> 0.3.2-1
- Python 3 port
- DM support
- 4K devices sizefix

* Mon Feb 20 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.1-1
- update version

* Sun Feb 19 2017 Stephane Thiell <sthiell@stanford.edu> 0.3.0-1
- update version

* Fri Dec  9 2016 Stephane Thiell <sthiell@stanford.edu> 0.2.5-1
- update version

* Mon Dec  5 2016 Stephane Thiell <sthiell@stanford.edu> 0.2.4-1
- update version

* Tue Nov  8 2016 Stephane Thiell <sthiell@stanford.edu> 0.2.3-1
- update version

* Mon Oct 31 2016 Stephane Thiell <sthiell@stanford.edu> 0.2.1-1
- update version

* Mon Oct 17 2016 Stephane Thiell <sthiell@stanford.edu> 0.1.7-1
- inception
