Name:           sensible-utils
Version:        0.0.12
Release:        5%{?dist}
Summary:        Utilities for sensible alternative selection

BuildArch:      noarch
License:        GPLv2+
URL:            https://packages.debian.org/unstable/admin/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/s/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  automake autoconf
BuildRequires:  make
BuildRequires:  po4a

# Needed by select-editor
Requires:       gettext

# Silence stderr when looking for $EDITOR, $VISUAL and $SELECTED_EDITOR (#1467077)
Patch0:         sensible-utils_stderr.patch
# Use --config instead of --list in update-alternatives --config editor (#1489159)
Patch1:         sensible-utils_editors.patch
# Just require gettext instead of installing a wrapper
Patch2:         sensible-utils_gettext.patch

%description
This package provides a number of small utilities which are used by programs to
sensibly select and spawn an appropriate browser, editor, or pager.


%prep
%autosetup -p1 -n %{name}.git


%build
# Needed for Patch2
autoreconf -ifv

%configure
%make_build


%install
%make_install


%files
%license debian/copyright
%doc debian/changelog
%{_bindir}/sensible-*
%{_bindir}/select-editor
%{_mandir}/man1/*.1*
%{_mandir}/*/man1/*.1*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Sandro Mani <manisandro@gmail.com> - 0.0.12-1
- Update to 0.0.12

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Sandro Mani <manisandro@gmail.com> - 0.0.11-1
- Update to 0.0.11

* Tue Oct 31 2017 Sandro Mani <manisandro@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.0.9-8
- Use --config instead of --list in update-alternatives --config editor

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Sandro Mani <manisandro@gmail.com> - 0.0.9-6
- Silence stderr when looking for $EDITOR, $VISUAL and $SELECTED_EDITOR (#1467077)
- Modernize spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Sandro Mani <manisandro@gmail.com> - 0.0.9-1
- Initial package
