%global oldpkg letsencrypt

# by default build Python 3 packages on Fedora and (RHEL >= 8)
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_without python3
%else
%bcond_with python3
%endif

# by default build NO Python 2 packages on (Fedora >= 30) and (RHEL >= 8)
%if (0%{?fedora} && 0%{?fedora} >= 30) || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_with python2
%else
%bcond_without python2
%endif

# build docs on Fedora but not on RHEL (not all sphinx packages available)
%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif

Name:           certbot
Version:        1.5.0
Release:        1%{?dist}
Summary:        A free, automated certificate authority client

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/certbot
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://certbot.eff.org/docs/install.html#certbot-auto
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg

Source10:       certbot-renew-systemd.service
Source11:       certbot-renew-systemd.timer
Source12:       certbot-sysconfig-certbot
Source13:       certbot-README.fedora

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-acme >= 1.4.0
BuildRequires:  python2-configargparse >= 0.9.3
BuildRequires:  python2-cryptography >= 1.2.3
BuildRequires:  python2-distro >= 1.0.1
BuildRequires:  python2-josepy >= 1.1.0
BuildRequires:  python2-mock
BuildRequires:  python2-pyrfc3339

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  pytest
BuildRequires:  python-configobj
BuildRequires:  python-devel
BuildRequires:  python-parsedatetime >= 1.3
BuildRequires:  python-setuptools
BuildRequires:  python-zope-component
BuildRequires:  python-zope-interface
BuildRequires:  pytz
%else
BuildRequires:  python2-configobj
BuildRequires:  python2-devel
BuildRequires:  python2-parsedatetime >= 1.3
BuildRequires:  python2-pytest
BuildRequires:  python2-pytz
BuildRequires:  python2-setuptools
BuildRequires:  python2-zope-component
BuildRequires:  python2-zope-interface
%endif

%if %{with docs}
# Required for documentation
BuildRequires:  python2-repoze-sphinx-autointerface
BuildRequires:  python2-sphinx >= 1.2.0
BuildRequires:  python2-sphinx_rtd_theme
%endif
%endif

%if %{with python3}
BuildRequires:  python3-acme >= 1.4.0
BuildRequires:  python3-configargparse >= 0.9.3
BuildRequires:  python3-configobj
BuildRequires:  python3-cryptography >= 1.2.3
BuildRequires:  python3-devel
BuildRequires:  python3-distro >= 1.0.1
BuildRequires:  python3-josepy >= 1.1.0
BuildRequires:  python3-parsedatetime >= 1.3
BuildRequires:  python3-pyrfc3339
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-component
BuildRequires:  python3-zope-interface


%if %{with docs}
# Required for documentation
BuildRequires:  python3-repoze-sphinx-autointerface
BuildRequires:  python3-sphinx >= 1.2.0
BuildRequires:  python3-sphinx_rtd_theme
%endif
%endif

# For the systemd macros
%{?systemd_requires}
BuildRequires:  systemd

# Used to verify OpenPGP signature
BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif

# Need to label the httpd rw stuff correctly until base selinux policy updated
Requires(post): %{_sbindir}/restorecon
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post): %{_sbindir}/semanage
%endif

# On F26+ and RHEL 8 use python3
%if (0%{?fedora} >= 26) || (0%{?rhel} && 0%{?rhel} >= 8)
Requires: python3-certbot = %{version}-%{release}
%else
Requires: python2-certbot = %{version}-%{release}
%endif

Obsoletes: %{oldpkg} < 0.6.0
Provides: %{oldpkg} = %{version}-%{release}

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%if %{with python2}
%package -n python2-certbot
Requires:       python2-acme >= 1.4.0
Requires:       python2-configargparse >= 0.9.3
Requires:       python2-cryptography >= 1.2.3
Requires:       python2-distro >= 1.0.1
Requires:       python2-josepy >= 1.1.0
# certbot.tests is considered part of the public API
Requires:       python2-mock
Requires:       python2-pyrfc3339

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
Requires:       python-configobj
Requires:       python-parsedatetime >= 1.3
Requires:       python-setuptools
Requires:       python-zope-component
Requires:       python-zope-interface
Requires:       pytz
%else
Requires:       python2-configobj
Requires:       python2-parsedatetime >= 1.3
Requires:       python2-pytz
Requires:       python2-setuptools
Requires:       python2-zope-component
Requires:       python2-zope-interface
%endif

Obsoletes:  python2-%{oldpkg} <  0.6.0
Provides:   python2-%{oldpkg} = %{version}-%{release}
Obsoletes:  python-%{oldpkg} <  0.6.0
Provides:   python-%{oldpkg} = %{version}-%{release}
#Recommends: certbot-doc
Summary:    Python 2 libraries used by certbot
%{?python_provide:%python_provide python2-certbot}

%description -n python2-certbot
The python2 libraries to interface with certbot

%endif

%if %{with python3}
%package -n python3-certbot
Requires:       python3-acme >= 1.4.0
Requires:       python3-configargparse
Requires:       python3-configobj
Requires:       python3-cryptography
Requires:       python3-distro
Requires:       python3-josepy >= 1.1.0
Requires:       python3-parsedatetime
Requires:       python3-pyrfc3339
Requires:       python3-pytz
Requires:       python3-zope-component
Requires:       python3-zope-interface

Summary:    Python 3 libraries used by certbot
%{?python_provide:%python_provide python3-certbot}

%description -n python3-certbot
The python3 libraries to interface with certbot

%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

# build documentation
# %%{__python2} setup.py install --user
# make -C docs  man PATH=${HOME}/.local/bin:$PATH

%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/certbot{,-2}
%endif
%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/certbot{,-3}
%endif
# Add compatibility symlink as requested by upstream conference call
ln -sf /usr/bin/certbot %{buildroot}/usr/bin/%{oldpkg}
# Put the man pages in place
# install -pD -t %%{buildroot}%%{_mandir}/man1 docs/_build/man/*1*
# Use python3 for F26+ or if python2 is disabled
%if 0%{?fedora} >= 26 || ! %{with python2}
ln -s %{_bindir}/certbot-3 %{buildroot}%{_bindir}/certbot
%else
ln -s %{_bindir}/certbot-2 %{buildroot}%{_bindir}/certbot
%endif
install -Dm 0644 %{SOURCE10} %{buildroot}%{_unitdir}/certbot-renew.service
install -Dm 0644 %{SOURCE11} %{buildroot}%{_unitdir}/certbot-renew.timer
install -Dm 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/certbot
mv %{SOURCE13} README.fedora

# project uses old letsencrypt dir for compatibility
install -dm 0755 %{buildroot}%{_sysconfdir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_sharedstatedir}/%{oldpkg}

%check
%if %{with python2}
cp -a setup.* README.rst tests build/lib/
(cd build/lib && %{__python2} setup.py test)
%endif
%if %{with python3}
%{__python3} setup.py test
%endif
# Make sure the scripts use the expected python versions
%if %{with python2}
grep -q %{__python2} %{buildroot}%{_bindir}/certbot-2
%endif
%if %{with python3}
grep -q %{__python3} %{buildroot}%{_bindir}/certbot-3
%endif

# The base selinux policies don't handle the certbot directories yet so set them up manually
%post
%if 0%{?rhel} && 0%{?rhel} <= 7
semanage fcontext -a -t cert_t '%{_sysconfdir}/(letsencrypt|certbot)/(live|archive)(/.*)?'
%endif
restorecon -R %{_sysconfdir}/letsencrypt || :

%files
%license LICENSE.txt
%doc README.rst README.fedora CHANGELOG.md
%{_bindir}/certbot
%{_bindir}/%{oldpkg}
# %%doc %%attr(0644,root,root) %%{_mandir}/man1/%%{name}*
%dir %{_sysconfdir}/%{oldpkg}
%dir %{_sharedstatedir}/%{oldpkg}
%config(noreplace) %{_sysconfdir}/sysconfig/certbot
%{_unitdir}/certbot-renew.service
%{_unitdir}/certbot-renew.timer

%if %{with python2}
%files -n python2-certbot
%license LICENSE.txt
%doc README.rst CHANGELOG.md
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}*.egg-info
%{_bindir}/certbot-2
%endif

%if %{with python3}
%files -n python3-certbot
%license LICENSE.txt
%doc README.rst CHANGELOG.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}*.egg-info
%{_bindir}/certbot-3
%endif

%changelog
* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843203)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831914)

* Sat Mar 21 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-3
- remove subpackage "python3-certbot-tests" which was committed by accident

* Mon Mar 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- add subpackage "python3-certbot-tests" on EPEL8

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809807)

* Sun Feb 23 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-2
- re-added "python-mock" as runtime dependency

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791087)

* Sun Feb 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-3
- do not strip "certbot.tests"

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Thu Dec 05 2019 Felix Schwarz <fschwarz@fedoraproject.org> 1.0.0-2
- adapt conditions for EPEL8
- remove runtime dependency on mock

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769107)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757575)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748612)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742577)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Sun Jun 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35.1-2
- Rebuilt to update automatic Python dependencies

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717677)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-3
- Fix build on Python 2

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-2
- Update --renew-hook to --deploy-hook (#1665755)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686184) (#1705300)
- Run renew timer twice daily with 12-hour random delay

* Wed Feb 13 2019 Eli Young <elyscape@gmail.com> - 0.31.0-2
- Fix acme dependency

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673769)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669313)

* Thu Jan 03 2019 Eli Young <elyscape@gmail.com> - 0.29.1-2
- Disable certbot-level randomized delay on renew
- Run certbot renew non-interactively

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627569)

* Mon Aug 20 2018 Eli Young <elyscape@gmail.com> - 0.26.1-2
- Properly create config and state directories (#1485745, #1613138)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600292)

* Thu Jul 12 2018 Eli Young <elyscape@gmail.com> - 0.26.0-1
- Update to 0.26.0 (#1600292)

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 0.25.1-5
- Clean up some rpmlint violations

* Wed Jun 27 2018 Eli Young <elyscape@gmail.com> - 0.25.1-4
- Update remaining python2 requirements for F27

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-3
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Eli Young <elyscape@gmail.com> - 0.25.1-2
- Make certbot depend on same version of python-certbot

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591031)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588219)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574140)
- Remove unnecessary patches

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563899)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558280)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552953)

* Thu Feb 08 2018 Eli Young <elyscape@gmail.com> - 0.21.1-5
- Remove SELinux policy management on Fedora
- Add temporary requirement on python-future

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 0.21.1-4
- Set permissions for certbot directories

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 0.21.1-3
- Regenerate dependencies from project (#1496291)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535995)

* Tue Jan 02 2018 Eli Young <elyscape@gmail.com> - 0.20.0-2
- Unify Fedora and EPEL7 specs

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499368)

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-2
- Fix deps

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Mon Sep 18 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-2
- Fix BuildRequires and Requires to use python2-* where applicable

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-3
- Further tweaks after upstream feedback
- On F26+ use python3

* Wed May 17 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-2
- Tweaks to the renew service bz#1444814

* Tue May 16 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.0-1
- Update to 0.14.0
- Fix for bz#1444814

* Fri Apr 28 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-2
- Incorrect target for timer

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
* Update to 0.13.0
- Timer tweaks bz#1441846
* Tue Mar 07 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-4
- Up the timer to daily at the request of upstream
* Mon Mar 06 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-3
- Label the certificates generated by certbot with correct selinux context
- Include optional timer for automated renewal
* Mon Mar 06 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-2
- upstream request not to use py3 yet so switch to py2 for default
- include a py3 option for testing
* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- update to 0.12.0
* Fri Feb 17 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-4
- change to python3 now certbot supports it
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-2
- parsedatetime needs future but doesn't declare it
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1
* Thu Jan 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.3-2
- Doc generation no longer needs sphinxcontrib-programoutput
- Work around Python dep generator dependency problem (#1410631)
* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Jul 06 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.8.1-2
- Remove sed-replace that changes help output and code behavior, closes #1348391
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
* Fri Jun 03 2016 james <james.hogarth@gmail.com> - 0.8.0-1
- update to 0.8.0 release
* Tue May 31 2016 James Hogarth <james.hogarth@gmail.com> - 0.7.0-1
- Update to 0.7.0
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-2
- Bump release to 2 since 1.0devXXX is greater than 1
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
* Thu May 12 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-1.0dev0git41f347d
- Update with compatibility symlink requested from upstream 
- Update with fixes from review
* Sun May 08 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-0.0dev0git38d7503
- Upgrade to 0.6.0 dev snapshot
- Rename to certbot to match upstream rename
* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 0.5.0-1
- Upgrade to 0.5.0
* Sat Mar 05 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-3
- Package does not require python-werkzeug anymore, upstream #2453
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-2
- Fix build on EL7 where no newer setuptools is available
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-1
- Upgrade to 0.4.2
* Tue Mar 1 2016 Nick Le Mouton <nick@noodles.net.nz> - 0.4.1-1
- Update to 0.4.1
* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
* Sat Jan 23 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.2.0-4
- Use acme dependency version consistently and add psutil min version
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-3
- Update the configargparse version in other places
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-2
- Update python-configargparse version requirement
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Apache plugin support for non-Debian based systems
- Relaxed PyOpenSSL version requirements
- Resolves issues with the Apache plugin enabling redirect
- Improved error messages from the client
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-2
- Fix packaging issues
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- fix a confusing UI path that caused some users to repeatedly renew their
- certs while experimenting with the client, in some cases hitting issuance rate limits
- numerous Apache configuration parser fixes
- avoid attempting to issue for unqualified domain names like "localhost"
- fix --webroot permission handling for non-root users
* Tue Dec 08 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.0-3
- Add python-sphinx_rtd_theme build requirement
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Add documentation from upstream
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-5.dev20151123
- Add missing build requirements that slipped through
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-4.dev20151123
- The python2 library should have the dependencies and not the bindir one
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3.dev20151123
- Separate out the python libraries from the application itself
- Enable python tests
* Tue Dec 01 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec to account for the runtime dependencies discovered
- Update spec to sit inline with current python practices
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
