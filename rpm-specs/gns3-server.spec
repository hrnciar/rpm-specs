# For pre-release
%global git_tag %{version}

# Filter auto-generated deps from bundled shell script (which depends on busybox only)
%global __requires_exclude_from ^%{python3_sitelib}/gns3server/compute/docker/resources/.*$

Name:           gns3-server
Version:        2.2.15
Release:        1%{?dist}
Summary:        Graphical Network Simulator 3

License:        GPLv3
URL:            http://gns3.com
Source0:        https://github.com/GNS3/gns3-server/archive/v%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1:        gns3.service
Patch0:         0001-changing-busybox-udhcpc-script-path.patch

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: python3-sphinx
BuildRequires: busybox

Requires: busybox
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends: docker
Recommends: qemu-kvm
%else
Requires: docker
Requires: qemu-kvm
%endif
Requires: python3-jsonschema >= 2.4.0
Requires: python3-aiohttp >= 2.2.0
Requires: python3-aiohttp-cors >= 0.5.1
Requires: python3-jinja2 >= 2.7.3
Requires: python3-raven >= 5.23.0
Requires: python3-psutil >= 3.0.0
Requires: python3-zipstream >= 1.1.4
Requires: python3-yarl >= 0.11
Requires: python3-prompt-toolkit
Requires: ubridge >= 0.9.14

Provides: bundled(busybox)


%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple
workstations to powerful routers.

This is the server package which provides an HTTP REST API for the client (GUI).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
%{name}-doc package contains documentation.


%prep
%autosetup -S git -n %{name}-%{git_tag}

# PR opened
sed -i '/typing/d' requirements.txt

# Relax requirements
sed -i 's|yarl.*|yarl>=0.11|' requirements.txt
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/\njsonschema>=2.6.0.*//g' requirements.txt
sed -i -r 's/sentry-sdk>=0.14.4.*//g' requirements.txt


%build
%py3_build

%install
%py3_install

# Remove shebang
find %{buildroot}/%{python3_sitelib}/ -name '*.py' -print \
   -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;
# Remove empty file
rm -f %{buildroot}/%{python3_sitelib}/gns3server/symbols/.gitkeep

# Build the doc1834283s
%{make_build} -C docs html
/bin/rm -f docs/_build/html/.buildinfo

## Systemd service part
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
mkdir -p  %{buildroot}%{_sharedstatedir}/gns3

## Remove tests: they are outside the namespace
rm -rf %{buildroot}/%{python3_sitelib}/tests/

## Don't bundle busybox with the package.
rm -f %{buildroot}/%{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox

%check


%files
%license LICENSE
%doc README.rst AUTHORS CHANGELOG
%{python3_sitelib}/gns3_server*.egg-info/
%ghost %{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox
%{python3_sitelib}/gns3server/
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_bindir}/gns3loopback
%{_unitdir}/gns3.service
%dir %attr(0755,gns3,gns3) %{_sharedstatedir}/gns3

%files doc
%license LICENSE
%doc docs/_build/html

%pre
getent group gns3 >/dev/null || groupadd -r gns3
getent passwd gns3 >/dev/null || \
       useradd -r -g gns3 -d /var/lib/gns3 -s /sbin/nologin \
               -c "gns3 server" gns3
exit 0

%post
[ -d "/var/lib/gns3" ] && chown -R gns3:gns3 %{_sharedstatedir}/gns3
%systemd_post gns3.service

# Replace bundled busybox with Fedora one
cp -f %{_sbindir}/busybox %{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox

%preun
%systemd_preun gns3.service

%postun
%systemd_postun_with_restart gns3.service

%changelog
* Wed Oct 07 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.15-1
- Update to 2.2.15

* Fri Sep 25 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.14-1
- Update to 2.2.14

* Wed Aug 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.12-1
- Update to 2.2.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.11-1
- Update to 2.2.11

* Tue Jun 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.10-1
- Update to 2.2.10

* Fri Jun 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.9-1
- Update to 2.2.9
- Fix docker image IP - rhbz#1834283

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.7-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.6-1
- Update to 2.2.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Fri Jan 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-2
- Add back a modern requires exclusion

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-1
- Update to 2.1.20
- Drop aiohttp bundle
- Fix optional dependencies with recommends - rhbz#1763762
- Don't distribute fedora busybox with the package.

* Sun Sep 15 2019 Othman Madjoudj <athmane@fedoraproject.org> - 2.1.16-7
- Add back Docker support (rhbz #1570826)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Athmane Madjoudj <athmane@fedoraproject.org>  - 2.1.16-3
- Add a patch to disable the broken embedded shell (rhbz #1690958)

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-2
- Fix typo in reqs
- Relax strict reqs

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-1
- Update to 2.1.16
- Fix broken deps (rhbz #1690958)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.11-1
- Update to 2.1.11 (rhbz #1581507)
- Drop unsued patch

* Wed Jul 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-2
- Add patch to fix py37 build (GH #1370)

* Mon Jul 16 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (rhbz #1581507)

* Mon Jul 16 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-4
- Rebuilt without bundled aiohttp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-3
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-3
- Fix issues reported by rpmlint

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-2
- Add option to bundle aiohttp since it gets broken very often

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (rhbz #1569276)

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-2
- Make sure to pull ubridge >= 0.9.14

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (rhbz #1554316)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (rhbz #1536429)

* Thu Jan 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (rhbz #1532422)

* Wed Jan 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.1-2
- Build docs with Python 3

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (rhbz #1528826)
- Remove non-needed workarounds

* Mon Nov 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 final
- Pick older libs as a temp bugs workaround

* Sat Nov 04 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc3
- Update to 2.1.0 RC3
- Relax version requirements

* Sun Oct 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc1
- Update to 2.1.0 RC1 which support recent aiohttp lib.

* Sun Jul 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-7
- Fix the reqs in prepration for 2.1 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-5
- Correct python3-aiohttp-cors version dep

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-4
- Bump release number for copr update

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-3
- Remove patch for aiohttp >= 2 since gns3 was instable
- Use the exact deps version as recommended by upstream

* Sat Jul 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-2
- Add a patch to support aiohttp >= 2

* Sat Jul 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Sat May 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-2
- Some spec fixes due to major version change

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Apr 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-3
- Add temporary workaround for py egg

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-2
- Remove some workarounds

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Sat Apr 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-2
- Add versioned deps

* Fri Feb 10 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-3
- Remove docker BR (not available in all arches)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Rebuild for Python 3.6

* Sun Sep 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2
- Remove upstreamed patches

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-4
- Fix typo in egg dir
- Build/ship the doc
- update BR

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org>  - 1.5.0-3
- Spec cleanup
- Add patch to move vmnet to gns3 namespace.
- Merge service sub pkg (too small)

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide a systemd service

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
