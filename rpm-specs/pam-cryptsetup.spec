%global commit 7b42892ea42cd710eab962236b3dd0ac55fbb402
%global shortcommit 7b42892
%global snapshot_date 20190823
%global snapinfo %{snapshot_date}.%{shortcommit}

Name:           pam-cryptsetup
Version:        0.1
Release:        0.5.%{snapinfo}%{?dist}
Summary:        PAM module for updating LUKS-encrypted volumes

License:        ASL 2.0
URL:            https://github.com/google/pam-cryptsetup/
# git archive --format=tar --prefix=pam-cryptsetup/ -o /tmp/pam-cryptsetup-0.1-$(git rev-parse --short HEAD).tar master
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# https://github.com/google/pam-cryptsetup/pull/9
Patch0:         %{name}-0.1-fix-stringop-truncation.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  cryptsetup-devel
BuildRequires:  device-mapper-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(glib-2.0)

%description
pam-cryptsetup provides a PAM module that allows LUKS-based disk encryption
passwords to be kept in sync with account passwords automatically based on
factors like if the user has decrypted the disk successfully previously.

The project as a whole consists of two parts: a PAM module pam_cryptsetup.so for
triggering on user authentication, and a helper program pam_cryptsetup_helper to
perform the actual encryption checks and modifications required.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
./autogen.sh
%configure
# Workaround libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' libtool
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/security/pam_cryptsetup.la


%check
# Only works if run as root outside of mock
# make check


%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/security/pam_cryptsetup.so
%{_libexecdir}/pam-cryptsetup



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20190823.7b42892
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20190823.7b42892
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1-0.3.20190823.7b42892
- Add missing BR on gcc
- Spec cleanup
- Make source downloadable

* Tue Mar  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1-0.2.20190823.7b42892
- Update patch to use #pragma to suppress stringop-truncation

* Fri Feb 14 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1-0.1.20190823.7b42892
- Initial package
