%global srcname flatpak-module-tools

Name:		%{srcname}
Version:	0.12
Release:	3%{?dist}
Summary:	Tools for maintaining Flatpak applications and runtimes as Fedora modules

License:	MIT
URL:		https://pagure.io/flatpak-module-tools
Source0:	https://releases.pagure.org/flatpak-module-tools/flatpak-module-tools-%{version}.tar.gz
Patch0:		0001-FlatpakBuilder-Fix-argument-passing-for-app-end-of-l.patch

BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel

Requires: module-build-service >= 2.25.0
Requires: python3-%{srcname} = %{version}-%{release}
Requires: python3-click
Requires: python3-koji
Requires: python3-requests

%description
flatpak-module-tools is a set of command line tools (all accessed via a single
'flatpak-module' executable) for operations related to maintaining Flatpak
applications and runtimes as Fedora modules.

%package -n python3-%{srcname}
Summary: Shared code for building Flatpak applications and runtimes from Fedora modules

# Note - pythonN-flatpak-modules-tools subpackage contains all the Python files from
# the upstream distribution, but some of them are only useful for the CLI, not
# for using this as a library for atomic-reactor. The dependencies here are those
# needed for library usage, the main package has the remainder.

Requires: flatpak
Requires: python3-libmodulemd
# For appstream-compose
Requires: libappstream-glib
# for SVG gdk-pixbuf loader
Requires: librsvg2
Requires: ostree
Requires: python3-jinja2
Requires: python3-six
Requires: python3-yaml

%description -n python3-%{srcname}
Python3 library for Flatpak handling

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.md
%{_bindir}/flatpak-module


%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/*

%changelog
* Mon Oct 05 2020 Kalev Lember <klember@redhat.com> - 0.12-3
- Fix argument passing for app end-of-life/end-of-life-rebase

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fedora <otaylor@redhat.com> - 0.12-1
- Version 0.12 - fix installing Flatpaks created by flatpak-1.6

* Tue Jul 14 2020 Owen Taylor <otaylor@redhat.com> - 0.11.5-1
- Version 0.11.5 - compatibility fixes for recent dnf and mock

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-4
- Rebuilt for Python 3.9

* Mon May 11 2020 Kalev Lember <klember@redhat.com> - 0.11.3-3
- Add xa.metadata as ostree commit metadata for runtimes
- Add support for end-of-life and end-of-life-rebase

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Owen Taylor <otaylor@redhat.com> - 0.11.3-1
- Version 0.11.3 - 0.11.2 had a stray file

* Fri Dec  6 2019 Owen Taylor <otaylor@redhat.com> - 0.11.2-1
- Version 0.11.2 - fix finish-args for runtimes

* Wed Oct 23 2019 Owen Taylor <otaylor@redhat.com> - 0.11.1-1
- Version 0.11.1 - compatibility with future versions of Flatpak that
  may generate label-only images

* Thu Oct 17 2019 Fedora <otaylor@redhat.com> - 0.11-1
- Version 0.11 - add standard labels, and allow using labels
  instead of annotations for Flatpak metadata.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Owen Taylor <otaylor@redhat.com> - 0.10.4-2
- Fix requirements

* Wed Jul 24 2019 Owen Taylor <otaylor@redhat.com> - 0.10.4-1
- Version 0.10.4 - fix bugs with libmodulemd v2 api conversion

* Fri Jul 12 2019 Owen Taylor <otaylor@redhat.com> - 0.10.1-1
- Version 0.10.1 - fix compatibility with newer module-build-service
  and avoid flatpak-repair issues.

* Mon Apr  1 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.3-1
- Version 0.9.3 - fix module-build-service and Flatpak compat issues

* Tue Feb  5 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.2-1
- Version 0.9.2 - fix icon validation for Flatpak 1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.1-1
- Version 0.9.1 - bug fixes including systemd-nspawn compatibility

* Tue Jan 22 2019 Owen Taylor <otaylor@redhat.com> - 0.9-1
- Version 0.9 - configurability, fixes for F29 dnf compatibility

* Fri Nov 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Drop python2 subpackage (#1634652)

* Thu Oct  4 2018 Owen Taylor <otaylor@redhat.com> - 0.8.4-1
- Version 0.8.4 - fix bugs in Flatpak installation

* Tue Oct  2 2018 Owen Taylor <otaylor@redhat.com> - 0.8.3-1
- Version 0.8.3 (bug fixes, add flatpak-module install --koji)

* Mon Sep 10 2018 Owen Taylor <otaylor@redhat.com> - 0.8.2-1
- Version 0.8.2 (Install flatpak-runtime-config with apps making
  included triggers work, support comments in finish-args,
  enable mock dnf cache for local builds.)
- Add dependencies on required tools

* Tue Aug 21 2018 Owen Taylor <otaylor@redhat.com> - 0.8.1-1
- Version 0.8.1 - bug fixes

* Fri Aug 10 2018 Owen Taylor <otaylor@redhat.com> - 0.8-1
- Version 0.8 - bug fixes and command line convenience

* Tue Jul 31 2018 Owen Taylor <otaylor@redhat.com> - 0.6-1
- Version 0.6 (improve container.yaml support)
- Build for Python2 as well
- Split out python<N>-flatpak-module-tools subpackages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuilt for Python 3.7

* Fri Jun  1 2018 Owen Taylor <otaylor@redhat.com> - 0.4-1
- Version 0.4 (fix container builds from Koji)

* Thu May 31 2018 Owen Taylor <otaylor@redhat.com> - 0.3-1
- Version 0.3 (minor fixes)

* Tue May 22 2018 Owen W. Taylor <otaylor@fishsoup.net> - 0.2-1
- Initial version
