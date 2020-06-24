%{?mingw_package_header}

Name:           mingw-wavpack
Version:        5.1.0
Release:        10%{?dist}
Summary:        Completely open audiocodec

License:        BSD
URL:            http://www.wavpack.com/
Source:         http://www.wavpack.com/wavpack-%{version}.tar.bz2
Patch1:         wavpack-0001-issue-27-do-not-overwrite-stack-on-corrupt-RF64-file.patch
Patch2:         wavpack-0002-issue-28-do-not-overwrite-heap-on-corrupt-DSDIFF-fil.patch
Patch3:         wavpack-0003-issue-28-fix-buffer-overflows-and-bad-allocs-on-corr.patch
Patch4:         wavpack-0004-issue-33-sanitize-size-of-unknown-chunks-before-mall.patch
Patch5:         wavpack-0005-issue-30-issue-31-issue-32-no-multiple-format-chunks.patch
Patch6:         wavpack-0006-issue-53-error-out-on-zero-sample-rate.patch
Patch7:         wavpack-0007-issue-54-fix-potential-out-of-bounds-heap-read.patch
Patch8:         wavpack-0008-issue-41-make-sure-DFF-chunk-does-not-have-negative-.patch
Patch9:         wavpack-0009-issue-43-catch-zero-channel-count-in-DSF-and-DSDIFF-.patch
# CVE-2019-1010315
Patch10:        wavpack-0010-issue-65-make-sure-DSDIFF-files-have-a-valid-channel.patch
Patch11:        wavpack-0011-issue-67-make-sure-sample-rate-is-specified-and-non-.patch
Patch12:        wavpack-0012-issue-68-clear-WaveHeader-at-start-to-prevent-uninit.patch
Patch13:        wavpack-0013-issue-66-make-sure-CAF-files-have-a-desc-chunk.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.


%package -n mingw32-wavpack
Summary:        %{summary}

%description -n mingw32-wavpack
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack library for the Win32 target.


%package -n mingw32-wavpack-tools
Summary:        %{summary} tools
Requires:       mingw32-wavpack = %{version}-%{release}

%description -n mingw32-wavpack-tools
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack tools for the Win32 target.


%package -n mingw64-wavpack
Summary:        %{summary}

%description -n mingw64-wavpack
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack library for the Win64 target.


%package -n mingw64-wavpack-tools
Summary:        %{summary} tools
Requires:       mingw64-wavpack = %{version}-%{release}

%description -n mingw64-wavpack-tools
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

This package is MinGW compiled wavpack tools for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n wavpack-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}
# remove libtool files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
# remove documentation (it's in the native version)
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%files -n mingw32-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw32_includedir}/wavpack
%{mingw32_bindir}/libwavpack-1.dll
%{mingw32_includedir}/wavpack/*.h
%{mingw32_libdir}/pkgconfig/*
%{mingw32_libdir}/libwavpack.dll.a

%files -n mingw32-wavpack-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw64_includedir}/wavpack
%{mingw64_bindir}/libwavpack-1.dll
%{mingw64_includedir}/wavpack/*.h
%{mingw64_libdir}/pkgconfig/*
%{mingw64_libdir}/libwavpack.dll.a

%files -n mingw64-wavpack-tools
%{mingw64_bindir}/*.exe


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 František Dvořák <valtri@civ.zcu.cz> - 5.1.0-9
- Autosetup macro
- Security fix for CVE-2018-10536, CVE-2018-10537, CVE-2018-10538,
  CVE-2018-10539, CVE-2018-10540
- Security fix for CVE-2018-19840, CVE-2018-19841
- Security fix for CVE-2019-11498, CVE-2019-1010315
- Security fix for CVE-2019-1010319
- Security fix for CVE-2019-1010317

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.1.0-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 František Dvořák <valtri@civ.zcu.cz> - 5.1.0-4
- Security fix for CVE-2018-6767, CVE-2018-7253, and CVE-2018-7254

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 David King <amigadave@amigadave.com> - 5.1.0-1
- Update to 5.1.0 (#1420680)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.80.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 David King <amigadave@amigadave.com> - 4.80.0-1
- Update to 4.80.0 (#1329173)
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.70.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 František Dvořák <valtri@civ.zcu.cz> - 4.70.0-1
- New release 4.70.0
- %%mingw_make_install macro deprecated

* Wed Feb 12 2014 František Dvořák <valtri@civ.zcu.cz> - 4.60.1-1
- Initial package
