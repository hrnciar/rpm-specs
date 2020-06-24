%global __python %__python3

Name:           dnf-plugin-diff
Version:        1.1
Release:        5%{?dist}
Summary:        Show local changes in RPM packages
BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/praiskup/%{name}
Source0:        https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

BuildRequires:  python3-devel

Requires:       cpio
Requires:       dnf
Requires:       file

Provides:       dnf-command(diff) = %version


%description
Dnf plugin to diff the original package contents against the locally changed
files.


%prep
%setup -q


%build
%configure PYTHON=python3
%make_build


%install
%make_install


%files
%license COPYING
%doc README
%_libexecdir/dnf-diff-*
%python3_sitelib/dnf-plugins


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- new release, fix for situation when package is provided by multiple
  repositories

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Pavel Raiskup <praiskup@redhat.com> - 1.0-2
- fix review issues spotted by Robert-André Mauchin

* Sat Dec 15 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0-1
- initial Fedora packaging
