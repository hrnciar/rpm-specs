Name:           inception
Version:        0.4.1
Release:        16%{?dist}
Summary:        A fireWire physical memory manipulation tool

License:        GPLv3+
URL:            http://www.breaknenter.org/projects/inception/
Source0:        https://github.com/carmaa/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch

# No FireWire on s390(x)
ExcludeArch:    s390 s390x

BuildRequires:  python3-devel

Requires:       kmod
Requires:       alsa-utils
Requires:       python3-forensic1394

%description
Inception is a FireWire physical memory manipulation and hacking tool
exploiting IEEE 1394 SBP-2 DMA. The tool can unlock (any password accepted)
and escalate privileges to Administrator/root on almost any machine you have
physical access to.

Inception aims to provide a stable and easy way of performing intrusive and
non-intrusive memory hacks on live computers using FireWire SBP-2 DMA. It is
primarily intended to do its magic against computers that utilize full disk
encryption such as BitLocker, FileVault, TrueCrypt or Pointsec.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md licenses/
%{_bindir}/incept
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info
%exclude %{python3_sitelib}/%{name}/test/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-16
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-13
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jun 20 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to new upstream release 0.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 11 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Update to new upstream release 0.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to new upstream release 0.3.5

* Mon Dec 02 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-2
- Remove test suite (#1036375)

* Thu Nov 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Update to new upstream release 0.3.3

* Wed Sep 04 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Update to new upstream release 0.3.0

* Mon Aug 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.6-1
- Update to new upstream release 0.2.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 13 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.4-1
- Update to new upstream versoin 0.2.4
- There is no firewire on s390
- Fix license

* Sat Dec 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-2
- Requirements fixed
- License fixed
- Switched to release tarball

* Tue Nov 20 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream release 0.2.2

* Sat Sep 29 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Initial spec file for Fedora
