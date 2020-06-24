Name:           qm-vamp-plugins
Version:        1.7.1
Release:        11%{?dist}
Summary:        Vamp audio feature extraction plugin

License:        GPLv2+
# original homepage: http://isophonics.net/QMVampPlugins
URL:            http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html
Source0:        https://code.soundsoftware.ac.uk/attachments/download/1604/qm-vamp-plugins-1.7.1.tar.gz
# build flags cleanup
# (part of it not intended for upstream)
# http://vamp-plugins.org/forum/index.php/topic,270.0.html
Patch0:         qm-vamp-plugins-build.patch
# unbundle qm-dsp
# (not intended for upstream)
Patch1:         qm-vamp-plugins-unbundle.patch

BuildRequires:  atlas-devel
BuildRequires:  gcc-c++
BuildRequires:  kiss-fft-static
BuildRequires:  qm-dsp-static
BuildRequires:  vamp-plugin-sdk-devel

%description
qm-vamp-plugins are vamp audio feature extraction plugins from the Centre for
Digital Music at Queen Mary, University of London,
http://www.elec.qmul.ac.uk/digitalmusic/.

This plugin set includes note onset detector, beat and barline tracker, tempo
estimator, key estimator, tonal change detector, structural segmenter, timbral
and rhythmic similarity, wavelet scaleogram, adaptive spectrogram, note
transcription, chromagram, constant-Q spectrogram, and MFCC plugins.

For more information see
http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html.


%prep
%setup -q
# remove atlas binaries
rm -rf build/linux/amd64 build/linux/i686
cp -p build/linux/Makefile.linux32 Makefile
# remove bundled qm-dsp, also with bundled kiss-fft
rm -rf qm-dsp
%patch0 -p1
%patch1 -p1


%build
# atlas libraries
%if 0%{?rhel} >= 7 || 0%{?fedora}
ATLAS_LIBS="-L%{_libdir}/atlas -ltatlas"
%else
ATLAS_LIBS="-L%{_libdir}/atlas -llapack -lcblas"
%endif

# extra cflags used in upstream
%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif

CFLAGS="-I%{_includedir}/qm-dsp $EXTRA_CFLAGS %{?optflags}" \
LDFLAGS="%{?__global_ldflags}" \
ATLAS_LIBS="$ATLAS_LIBS" \
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}/vamp
install -p -m 0644 qm-vamp-plugins.cat %{buildroot}%{_libdir}/vamp/
install -p -m 0644 qm-vamp-plugins.n3 %{buildroot}%{_libdir}/vamp/
install -p -m 0755 qm-vamp-plugins.so %{buildroot}%{_libdir}/vamp/


%files
%license COPYING
%doc README.txt
%{_libdir}/vamp/qm-vamp-plugins.cat
%{_libdir}/vamp/qm-vamp-plugins.n3
%{_libdir}/vamp/qm-vamp-plugins.so


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-8
- Add gcc-c++ BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-1
- Update to 1.7.1 (#1261681)
- New homepage
- Unbundled qm-dsp and kiss-fft libraries
- Rebased build patch
- New packaging guidelines (license tag)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 05 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-2
- Replace qm-dsp-devel for qm-dsp-static BR
- Part of the build flags patch sent upstream

* Sat Feb 1 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-1
- Initial package
