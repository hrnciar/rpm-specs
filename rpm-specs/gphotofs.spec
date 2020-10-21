Summary: A FUSE filesystem module to mount your camera as a filesystem
Name: gphotofs
Version: 0.5
Release: 13%{?dist}
License: GPL+
URL: http://www.gphoto.org/proj/gphotofs/
BuildRequires:  gcc
BuildRequires: glib2-devel, fuse-devel, libgphoto2-devel
Source0: http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2

%description
A filesystem client based on libgphoto2 that exposes supported cameras
as filesystems; while some cameras implement the USB Mass Storage class
and already appear as filesystems (making this program redundant), many
use the Picture Transfer Protocol (PTP) or some other custom protocol.
But as long as the camera is supported by libgphoto2, it can be mounted
as a filesystem using this program.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS COPYING README NEWS ChangeLog

%{_bindir}/gphotofs

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-2
- Rebuild (libgpohoto2)

* Thu Sep 18 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5-1
- Initial release
