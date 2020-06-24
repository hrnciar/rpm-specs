%global binname qt5-virt-manager

Name:           qt-virt-manager
Version:        0.70.91
Release:        4%{?dist}
Summary:        Qt Virtual Machine Manager

License:        GPLv2+
URL:            http://f1ash.github.io/%{name}
Source0:        https://github.com/F1ash/%{name}/archive/%{version}.tar.gz

# be compatible with prior subpackages
Provides:       virt-manager-qt4 = %{version}-%{release}
Provides:       virt-manager-qt5 = %{version}-%{release}
Provides:       bundled(krdc-libs)
Provides:       bundled(qterminal)
Obsoletes:      virt-manager-qt4 <= 0.25.47
Obsoletes:      virt-manager-qt5 <= 0.25.47

Requires:       hicolor-icon-theme

Requires:       libvirt
Requires:       qtermwidget >= 0.7.1
Requires:       qt-remote-viewer

# for use qemu-kvm (more useful)
Requires:       qemu-kvm

# for use SPICE viewer
Requires:       spice-vdagent
# for use VNC viewer
Requires:       krdc-libs

# optional runtime extensions
%if 0%{?fedora}
# for scrubbing
Suggests:       scrub
# for use VNC client with tls
Suggests:       gnutls
%endif

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qtermwidget-devel >= 0.7.1
BuildRequires:  qt5-linguist

BuildRequires:  libvirt-devel
BuildRequires:  glibc-headers
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  spice-protocol
BuildRequires:  spice-glib-devel
BuildRequires:  libvncserver-devel
BuildRequires:  krdc-devel
%if 0%{?fedora}
%global libcacard 1
BuildRequires:  libcacard-devel
%endif

%description
Qt Virtual Machine Manager provides a graphical tool for
administering virtual machines for QEMU/KVM, Xen, LXC, OpenVZ,
VBox, VMWare, HyperV, IBM PowerVM, Bhyve virtual machines
and other Virtual Entities.
Start, stop, add or remove virtual devices, connect to a
graphical or serial console, and see resource usage
statistics for existing VMs on local or remote machines.
Uses libvirt as the back-end management API.
Uses Spice/VNC viewers for control.

%package -n     qt-remote-viewer
Summary:        Qt Remote Viewer

%description -n qt-remote-viewer
Qt viewer for remote access to Spice/VNC desktops.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake .. \
  -DBUILD_QT_VERSION=5 \
  %{?libcacard:-DWITH_LIBCACARD=1}

popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{binname}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/qt5-remote-viewer.desktop

%files
%license LICENSE Licenses
%doc README.md Changelog
%{_bindir}/%{binname}
%{_datadir}/applications/%{binname}.desktop
%{_datadir}/%{binname}/
%{_datadir}/icons/hicolor/*/apps/virtual-engineering.*

%files -n       qt-remote-viewer
%license LICENSE
%{_bindir}/qt5-remote-viewer
%{_datadir}/applications/qt5-remote-viewer.desktop
%{_datadir}/icons/hicolor/*/apps/remote-desktop-viewer.*
%{_datadir}/mime/packages/qt-remote-viewer-mime.xml


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Fl@sh <kaperang07@gmail.com> - 0.70.91-1
- version updated;

* Thu Jul 12 2018 Fl@sh <kaperang07@gmail.com> - 0.70.90-1
- version updated;

* Fri Apr 20 2018 Fl@sh <kaperang07@gmail.com> - 0.60.88-3
- added bundled qterminal Provides;
- release updated;

* Sat Apr 14 2018 Fl@sh <kaperang07@gmail.com> - 0.60.88-2
- added bundled krdc Provides;
- release updated;

* Sat Apr 14 2018 Fl@sh <kaperang07@gmail.com> - 0.60.88-1
- added krdc BR, R;
- version updated;

* Mon Apr 02 2018 Raphael Groner <projects.rg@smart.ms> - 0.57.86-1
- new version

* Thu Mar 15 2018 Fl@sh <kaperang07@gmail.com> - 0.53.83-1
- version updated;

* Sun Mar  4 2018 Fl@sh <kaperang07@gmail.com> - 0.52.81-1
- version updated;

* Sat Feb 24 2018 Fl@sh <kaperang07@gmail.com> - 0.52.80-2
- release updated;

* Thu Feb 22 2018 Fl@sh <kaperang07@gmail.com> - 0.52.80-1
- version updated;

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.79-2
- Remove obsolete scriptlets

* Sat Jan  6 2018 Fl@sh <kaperang07@gmail.com> - 0.48.79-1
- version updated;

* Mon Oct 16 2017 Rex Dieter <rdieter@fedoraproject.org> 0.45.75-1
- 0.45.75, fix some %%fedora macros

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
 
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Fl@sh <kaperang07@gmail.com> - 0.43.72-1
- version updated;
 
* Sat May 13 2017 Fl@sh <kaperang07@gmail.com> - 0.43.70-2
- return R and BR to previous state;
- release updated;

* Fri May 12 2017 Fl@sh <kaperang07@gmail.com> - 0.43.70-1
- enhanced %%description;
- remove Qt4 build part;
- version updated;

* Fri Mar 17 2017 Fl@sh <kaperang07@gmail.com> - 0.42.67-1
- enhanced %%description;
- version updated;

* Mon Jan 30 2017 Fl@sh <kaperang07@gmail.com> - 0.39.60-1
- removed libvirt-daemon-driver-qemu, libvncserver R;
- version updated;

* Tue Oct 18 2016 Fl@sh <kaperang07@gmail.com> - 0.37.57-1
- version updated;
- added changes for qt-remote-viewer subpackages;

* Wed Oct  5 2016 Fl@sh <kaperang07@gmail.com> - 0.37.56-1
- version updated;

* Wed Sep 21 2016 Fl@sh <kaperang07@gmail.com> - 0.36.55-1
- version updated;
- added remote-desktop-viwer into %%check and %%files;

* Sat Jul 16 2016 Fl@sh <kaperang07@gmail.com> - 0.34.50-1
- version updated;

* Wed May 11 2016 Fl@sh <kaperang07@gmail.com> - 0.27.50-1
- version updated;
- clear %%changelog;
