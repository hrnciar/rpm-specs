%global gitrev 51f87891081840a7ea3cd6ad8d43062b3d35f1c8
%global shortgit 51f87891081840a

Name:           piglit
Version:        1.0.20200330
Release:        1.git51f87891081840a%{?dist}
Summary:        Collection of automated tests for OpenGL implementations

License:        MIT and GPLv2+ and GPLv3 and LGPLv2
URL:            https://gitlab.freedesktop.org/mesa/piglit/
# git clone git://anongit.freedesktop.org/piglit && cd piglit
# git archive --prefix=piglit/ HEAD|bzip2>piglit.tar.bz2
Source0:        %{URL}/-/archive/%{gitrev}/piglit-%{shortgit}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  chrpath
BuildRequires:  waffle-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXrender-devel
BuildRequires:  pkgconfig(dri), pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  ocl-icd-devel opencl-headers
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  python >= 2.7
BuildRequires:  numpy >= 1.7.0
BuildRequires:  python-mako >= 0.7.3
BuildRequires:  python-nose
BuildRequires:  python-lxml
BuildRequires:  python-six >= 1.5.2
Requires:       python-mako >= 0.8.0
%else
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-numpy >= 1.7.0
BuildRequires:  python3-mako >= 0.8.0
BuildRequires:  python3-nose
BuildRequires:  python3-lxml
BuildRequires:  python3-six >= 1.5.2
Requires:       python3-mako >= 0.8.0
%endif
Requires:       /usr/bin/clinfo


%description
Piglit is a collection of automated tests for OpenGL implementations.

The goal of Piglit is to help improve the quality of open source
OpenGL drivers by providing developers with a simple means to
perform regression tests.

%prep
%autosetup -n %{name}-%{gitrev}

rm -rf build
mkdir build

%build
pushd build

%cmake ../ \
%ifarch i686
    -DCMAKE_C_FLAGS_DEBUG:STRING=-O0 -DCMAKE_CXX_FLAGS_DEBUG:STRING=-O0 \
%endif
    -DCMAKE_BUILD_TYPE:STRING=Debug \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DPIGLIT_BUILD_CL_TESTS=1

  make VERBOSE=1 %{?_smp_mflags}

popd

%install
pushd build
  %make_install
popd

# We don't want this in its own doc directory.
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

# And bash completion is more bother than use for the real testing
rm -fv %{buildroot}%{_datadir}/bash-completion


%files
%license COPYING licences/*
%doc README.md HACKING RELEASE examples
%{_bindir}/%{name}
%{_libdir}/%{name}/


%changelog
* Mon Mar 30 2020 Dave Airlie <airlied@redhat.com> - 1.0.20200330-1.git51f87891081840a
- Update to latest to avoid ftbfs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20171027-12.GIT65b4b197
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20171027-11.GIT65b4b197
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20171027-10.GIT65b4b197
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20171027-9.GIT65b4b197
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20171027-8.GIT65b4b197
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Adam Jackson <ajax@redhat.com> - 1.0.20171027-7.GIT65b4b197
- New git snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20170515-6.GITa969d23f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20170515-5.GITa969d23f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Matěj Cepl <mcepl@redhat.com> - 1.0.20170515-4.GITa969d23f
- New release required for testing of Vulcan.

* Tue Feb 21 2017 Matěj Cepl <mcepl@redhat.com> - 1.0.20170221-4.git2e97840
- Upgrading to the latest checkout.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20160901-3.git2401e47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Adam Jackson <ajax@redhat.com> - 1.0.20160831-2.git2401e479
- Spell python3-mako correctly

* Thu Jul 30 2015 Matej Cepl <mcepl@redhat.com> - 1-0.25.20150206GITi9c8b329
- Add python-mako Requires (RHBZ# 1247936)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.24.20150206GITi9c8b329
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1-0.23.20150206GITi9c8b329
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 06 2015 Matej Cepl <mcepl@redhat.com> - 1-0.22.20150206GITi9c8b329
- Upgrade to the latest git checkout.

* Tue Jan 6 2015 Matěj Cepl <mcepl@redhat.com> - 1-0.21.20150103GIT4adb082
- Upgrade to the latest upstream release. (RHBZ# 1177151)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.20.20140414GIT8775223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.19.20140414GIT8775223
- Add ExcludeArch for EPEL-6 and ppc64 properly (RHBZ# 1093720)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-0.18.20140414GIT8775223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.17.20140414GIT8775223
- Except I have created condition incorrectly.

* Fri May 16 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.16.20140414GIT8775223
- importlib is since python 2.7 in the standard library, no need to
  import it.

* Thu May 15 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.15.20140414GIT8775223
- Put ExcludeArch back for ppc64.
- Add python-importlib Require

* Tue Apr 15 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.14.20140414GIT8775223
- Remove ExcludeArch

* Mon Apr 14 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.13.20140414GIT8775223
- New upstream checkout (our patches were upstreamed)

* Thu Mar 20 2014 Matěj Cepl <mcepl@redhat.com> - 1-0.13.20140320GITb561c3c
- New upstream checkout.

* Wed Oct 23 2013 Matěj Cepl <mcepl@redhat.com> - 1-0.13.20131023GITe2db751
- New upstream checkout.

* Sat Aug 24 2013 Matěj Cepl <mcepl@redhat.com> - 1-0.13.20130824GITbccdf6f
- New upstream checkout.

* Fri Jan 13 2012 Matěj Cepl <mcepl@redhat.com> 1-0.12.git20120110Rf26fbd0
- more cleanup to (almost) satisfy formal review.

* Fri Jan 13 2012 Matěj Cepl <mcepl@redhat.com> 1-0.11.git20120110Rf26fbd0
- New patch from http://article.gmane.org/gmane.comp.video.piglit/98/
- Actually really use %%cmake macro

* Thu Jan 12 2012 Matěj Cepl <mcepl@redhat.com> 1-0.10.git20120110Rf26fbd0
- add -DBUILD_SHARED_LIBS:BOOL=OFF to the cmake call to workaround FTBFS
- remove unnecessary executable bits and shebangs

* Tue Jan 10 2012 Matěj Cepl <mcepl@redhat.com> 1-0.9.git20120110Rf26fbd0
- New upstream checkout, preparing for the Fedora submission.

* Mon Dec 19 2011 Matěj Cepl <mcepl@redhat.com> 1-0.8.git20111219R8749563
- Upgrade to the latest upstream checkout

* Tue Nov 29 2011 Matěj Cepl <mcepl@redhat.com> - 1-0.8.git20111129R6a241f7
- Upgrade to the latest upstream checkout

* Mon Nov 28 2011 Matěj Cepl <mcepl@redhat.com> - 1-0.7.git20111107R228aaeb
- Exclude archs, add libXrender-devel as a build requirement.

* Tue Oct 18 2011 'Matěj Cepl <mcepl@redhat.com>' - 1-0.6.git20111018R5078a37
- New upstream checkout
- Copy also piglit*.py files to libdir. *PALMFACE*

* Mon Oct 17 2011 'Matěj Cepl <mcepl@redhat.com>' - 1-0.5.git20111017reaa3617a
- New upstream checkout.

* Mon Oct 17 2011 Matěj Cepl <mcepl@redhat.com> - 1-0.5.git20111017reaa3617a
- Update to the latest upstream checkout.

* Sat Oct 08 2011 Matěj Cepl <mcepl@redhat.com> - 1-0.4.git20111007r7fe681a0
- First package.


# vi:sw=4 ts=8 et
