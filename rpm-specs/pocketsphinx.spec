%global extraver prealpha

Name:           pocketsphinx
Version:        5
Release:        0.5.%{extraver}%{?dist}
Epoch:          1
Summary:        Real-time speech recognition

License:        BSD
URL:            http://cmusphinx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}%{extraver}.tar.gz

BuildRequires:  autoconf-archive
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(sphinxbase)
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-models

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package devel
Summary:        Header files for developing with pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig(sphinxbase)
Provides:       bundled(jquery)

%description devel
Header files for developing with pocketsphinx.

%package libs
Summary:        Shared libraries for pocketsphinx executables

%description libs
Shared libraries for pocketsphinx executables.

%package models
Summary:        Voice and language models for pocketsphinx
BuildArch:      noarch

%description models
Voice and language models for pocketsphinx.

%package plugin
Summary:        Pocketsphinx gstreamer plugin
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-plugins-base%{?_isa}

%description plugin
A gstreamer plugin for pocketsphinx.

%package -n python3-pocketsphinx
%{?python_provide:%python_provide python3-pocketsphinx}
Summary:        Python interface to pocketsphinx
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-sphinxbase%{?_isa}

%description -n python3-pocketsphinx
Python interface to pocketsphinx.

%prep
%setup -q -n %{name}-%{version}%{extraver}

# Force code generation with a newer version of Cython
rm -f python/pocketsphinx.c

# Use system-provided ax_python_devel.m4
rm -f m4/ax_python_devel.m4

# Regenerate files due to m4 change
autoreconf -fi

%build
export PYTHON="python3"
%configure --disable-static --with-python=%{__python3}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

make %{?_smp_mflags}

%install
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}
mkdir -p $RPM_BUILD_ROOT%{python3_sitearch}
%make_install

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

# Get rid of files we don't want packaged
find $RPM_BUILD_ROOT%{_libdir} -name \*.la | xargs rm -f
rm -f doc/html/installdox

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files models
%{_datadir}/%{name}/

%files plugin
%{_libdir}/gstreamer-1.0/*

%files -n python3-pocketsphinx
%{python3_sitearch}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.5.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:5-0.4.prealpha
- Rebuilt for Python 3.9

* Wed May 13 2020 W. Michael Petullo <mike@flyn.org> - 1:5-0.3.prealpha
- Fix incorrect version after incrementing the wrong number

* Wed May 13 2020 W. Michael Petullo <mike@flyn.org> - 1:6-0.2.prealpha
- Fix GStreamer dependency for plugin package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.2.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 W. Michael Petullo <mike@flyn.org> - 1:5-0.1.prealpha
- More work to switch to Python 3
- Adjust version convention to match un-retired sphinxbase

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5prealpha-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5prealpha-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5prealpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 5prealpha-2
- Switch to Python 3

* Sun Jul 22 2018 W. Michael Petullo <mike@flyn.org> - 5prealpha-1
- New upstream release

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-21
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-18
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-17
- Python 2 binary package renamed to python2-pocketsphinx
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Jerry James <loganjerry@gmail.com> - 0.8-12
- Support long utterances (bz 1356809)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 0.8-9
- Rebuild for sphinxbase linked with atlas
- Add Provides: bundled(jquery)
- Minor spec file cleanups

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep  5 2013 Jerry James <loganjerry@gmail.com> - 0.8-6
- Split the voice and language models into a noarch subpackage due to size

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 0.8-4
- Different approach to the -largefile patch to fix problems with the original
- Drop -aarch64 patch since we now run autoreconf
- Add -doxygen patch to fix broken doxygen comments

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 0.8-3
- Add -largefile patch for large file support
- Add -aarch64 patch (bz 926360)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 0.7-4
- Rebuild for bz 772699
- New project URL

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.7-3
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Fri Jul 15 2011 Jerry James <loganjerry@gmail.com> - 0.7-2
- Use RPM 4.9's new filter scheme to remove bogus provides
- Minor spec file cleanups

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream release
- All sources are now BSD

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-4
- Update python BRs for Rawhide

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-3
- More review issues:
- Fix license (gstreamer plugin is LGPLv2+)
- Remove unnecessary zero-byte turtle dictionary file

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-2
- Fix issues raised in review by Andrew Colin Kissa, namely:
- Improve description and summary
- Change the group to Applications/Multimedia

* Tue Mar 24 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jul 10 2008 Jerry James <loganjerry@gmail.com> - 0.5-1
- Update to 0.5

* Wed Mar  5 2008 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- Initial RPM
