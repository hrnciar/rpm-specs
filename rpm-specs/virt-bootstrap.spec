Name: virt-bootstrap
Version: 1.1.1
Release: 9%{?dist}
Summary: System container rootfs creation tool

License: GPLv3+
URL: https://github.com/virt-manager/virt-bootstrap
Source0: http://virt-manager.org/download/sources/virt-bootstrap/%{name}-%{version}.tar.gz

# Upstream patches

BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/git
BuildRequires: python3-devel
BuildRequires: python3-libguestfs
BuildRequires: python3-passlib
BuildRequires: python3-setuptools
BuildRequires: fdupes

Requires: python3-libguestfs
Requires: python3-passlib
Requires: skopeo
Requires: libvirt-sandbox

BuildArch: noarch

%description
Provides a way to create the root file system to use for
libvirt containers.

%prep
%autosetup -S git

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{_prefix}

# Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f -executable -print); do
    sed -i '1 s/^#!\/usr\/bin\/env python3/#!%{__python3}/' $f || :
done

# Delete '#!/usr/bin/env python'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f \! -executable -print); do
    sed -i '/^#!\/usr\/bin\/env python/d' $f || :
done

%files
%license LICENSE
%doc README.md ChangeLog AUTHORS
%{_bindir}/virt-bootstrap
%{python3_sitelib}/virtBootstrap
%{python3_sitelib}/virt_bootstrap-*.egg-info
%{_mandir}/man1/virt-bootstrap*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Fabiano Fidêncio <fabiano@fidencio.org> - 1.1.1-1
- Update to new upstream release: 1.1.1
- Resolves: rhbz#1727771

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Thu May 31 2018 Fabiano Fidêncio <fabiano@fidencio.org> -1.1.0-1
- Update to new upstream release: 1.1.0

* Thu May 17 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 1.0.0-2
- Set "BuildArch: noarch" as this is an arch independent package
- Drop "Buildroot" tag as it's obsolete
- Drop "%%defattr" tag as it's obsolete
- Add "BuildRequires: /usr/bin/git" (due to %%autosetup -S git)
- Add a note to make clear that the patches are backported from upstream
- Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
- Delete '#!/usr/bin/env python' from non executable files

* Wed May 16 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 1.0.0-1
- Initial release
