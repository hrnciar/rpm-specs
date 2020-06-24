Name:           rsync-bpc
Version:        3.1.2.0
Release:        4%{?dist}
Summary:        A customized version of rsync that is used as part of BackupPC

License:        GPLv3+
URL:            https://github.com/backuppc/rsync-bpc
Source0:        https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  popt-devel

Provides:       bundled(rsync)


%description
Rsync-bpc is a customized version of rsync that is used as part of
BackupPC, an open source backup system.

The main change to rsync is adding a shim layer (in the subdirectory
backuppc, and in bpc_sysCalls.c) that emulates the system calls for
accessing the file system so that rsync can directly read/write files
in BackupPC's format.

Rsync-bpc is fully line-compatible with vanilla rsync, so it can talk
to rsync servers and clients.

Rsync-bpc serves no purpose outside of BackupPC.


%prep
%autosetup -n %{name}-%{version}


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc NEWS README
%{_bindir}/rsync_bpc


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Richard Shaw <hobbes1069@gmail.com> - 3.1.2.0-1
- Update to 3.1.2.0.

* Tue Nov 27 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.13-1
- Update to 3.0.9.13.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.12-1
- Update to 3.0.9.12.

* Sun Dec 17 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.11-1
- Update to latest upstream release, 3.0.9.11.

* Mon Dec  4 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.9-1
- Update to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.8-1
- Update to latest upstream release.

* Sun May 28 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.7-1
- Update to latest upstream release.

* Sat Mar 25 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.6-1
- Update to latest upstream release.

* Sat Mar 18 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.5-1
- Several spec file updates.

* Mon Mar 13 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.5-1
- Initial packaging.
