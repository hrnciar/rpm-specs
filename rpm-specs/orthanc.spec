%define orthancversion 1.5.4


Name:		orthanc
Version:	%{orthancversion}
Release:	7%{?dist}
Summary:	RESTful DICOM server for healthcare and medical research

License:	GPLv3 with exceptions
URL:		http://www.orthanc-server.com/
Source0:	http://www.orthanc-server.com/downloads/get.php?path=/orthanc/Orthanc-%{version}.tar.gz
Source1:	orthanc.service
Source2:	orthanc.json
Source3:        serve-folders.json
Source4:        worklists.json
Source5:        index.html

# This patch fixes the installation path of the 64bit version of the plugins
Patch1:		orthanc-%{orthancversion}-lib64.patch

BuildRequires:  gcc-c++
BuildRequires:	cmake >= 2.8.0
BuildRequires:	help2man
BuildRequires:	python3-devel
BuildRequires:	doxygen
BuildRequires:	systemd
BuildRequires:	/usr/bin/pathfix.py

BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	dcmtk-devel
BuildRequires:	gtest-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsqlite3x-devel
BuildRequires:	libuuid-devel
BuildRequires:	lua-devel >= 5.1.0
BuildRequires:	mongoose-devel
BuildRequires:	openssl-devel
BuildRequires:	pugixml-devel

%if 0%{?fedora} >= 24
# For linking against "libxml2.so"
BuildRequires:  libxml2-devel
%endif

# The following line is required to add the "orthanc" user and group
Requires(pre):	shadow-utils

# The following lines are required to install the Systemd service
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets?rd=Packaging/ScriptletSnippets#Macroized_scriptlets_.28Fedora_18.2B.29
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Orthanc aims at providing a simple, yet powerful standalone DICOM
server. Orthanc can turn any computer running Windows or Linux into a
DICOM store (in other words, a mini-PACS system). Its architecture is
lightweight, meaning that no complex database administration is
required, nor the installation of third-party dependencies.

What makes Orthanc unique is the fact that it provides a RESTful
API. Thanks to this major feature, it is possible to drive Orthanc
from any computer language. The DICOM tags of the stored medical
images can be downloaded in the JSON file format. Furthermore,
standard PNG images can be generated on-the-fly from the DICOM
instances by Orthanc.

Orthanc lets its users focus on the content of the DICOM files,
hiding the complexity of the DICOM format and of the DICOM protocol.



%package -n orthanc-devel
Summary:        Header files for creating Orthanc plugins

# Guideline for header only libraries
Provides:       orthanc-static = %{version}-%{release}

%description -n orthanc-devel
This package includes the header files to develop C/C++ plugins
for Orthanc.


   
%package -n orthanc-doc
Summary:        Documentation files for Orthanc
BuildArch:	noarch

%description -n orthanc-doc
This package includes the documentation and the sample codes
available for Orthanc. It also includes the documentation
to develop C/C++ plugins for Orthanc.



%prep
%setup -q -n Orthanc-%{version}
%patch1

# Copy the configuration file and the Systemd Service for the Orthanc server
cp -p %SOURCE1 orthanc.service

# Fix Python shebangs
# https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error#Using_pathfix.py_to_fix_shebangs
pathfix.py -i "%{__python3} %{py3_shbang_opts}" -p -n .

%build
%cmake	. \
	-DCMAKE_BUILD_TYPE=Release \
	-DDCMTK_LIBRARIES=CharLS \
	-DSTANDALONE_BUILD:BOOL=ON \
	-DSTATIC_BUILD:BOOL=OFF \
	-DENABLE_CIVETWEB:BOOL=OFF \
	-DSYSTEM_MONGOOSE_USE_CALLBACKS=OFF \
	-DUNIT_TESTS_WITH_HTTP_CONNEXIONS=OFF

make %{?_smp_mflags}

# Generate the man page
help2man ./Orthanc -N -n "Lightweight, RESTful DICOM server for healthcare and medical research" > Orthanc.1


%check
# Execute the unit tests
# TODO - Check out why "PngWriter.ColorPattern" fails on Fedora 28,
# but only with architecture "aarch64"
# TODO - Check out why "Toolbox.CaseWithAccents" fails on Fedora 30 (but OK on Fedora 28 and 29)
./UnitTests --gtest_filter=-PngWriter.ColorPattern:Toolbox.CaseWithAccents


%install
make install DESTDIR=%{buildroot}

install -m 755 -d %{buildroot}%{_mandir}/man1
cp Orthanc.1 %{buildroot}%{_mandir}/man1

install -m 755 -d %{buildroot}%{_sysconfdir}/orthanc
cp %SOURCE2 %{buildroot}%{_sysconfdir}/orthanc
cp %SOURCE3 %{buildroot}%{_sysconfdir}/orthanc
cp %SOURCE4 %{buildroot}%{_sysconfdir}/orthanc

install -m 755 -d %{buildroot}%{_unitdir}
cp orthanc.service %{buildroot}%{_unitdir}

install -m 755 -d %{buildroot}%{_sharedstatedir}/orthanc/db-v6

# Move the plugins from "/usr/lib64/" to "/usr/lib64/orthanc", and
# remove the symbolic links generated by CMake
mkdir -p %{buildroot}%{_libdir}/orthanc
mv %{buildroot}%{_libdir}/*.so.%{orthancversion} %{buildroot}%{_libdir}/orthanc
rm %{buildroot}%{_libdir}/*.so

# Create symbolic links to plugins in "/usr/share/orthanc/plugins"
# We stick to the "relative symlinks" section of the guideline
mkdir -p %{buildroot}%{_prefix}/share/orthanc/plugins
ln -s ../../../..%{_libdir}/orthanc/libServeFolders.so.%{orthancversion} \
   %{buildroot}%{_prefix}/share/orthanc/plugins/libServeFolders.so
ln -s ../../../..%{_libdir}/orthanc/libModalityWorklists.so.%{orthancversion} \
   %{buildroot}%{_prefix}/share/orthanc/plugins/libModalityWorklists.so

# Prepare documentation: "index.html", Doxygen of plugin SDK, and sample codes
cp -r %SOURCE5 %{buildroot}%{_docdir}/orthanc/
cp -r Resources/Samples/ %{buildroot}%{_docdir}/orthanc/Samples
cp -r Plugins/Samples/ %{buildroot}%{_docdir}/orthanc/OrthancPluginSamples


%files
%doc AUTHORS COPYING NEWS README TODO
%{_mandir}/man1/Orthanc.1*
%{_bindir}/OrthancRecoverCompressedFile
%{_sbindir}/Orthanc
%{_unitdir}/orthanc.service
%{_libdir}/orthanc/*.so.%{orthancversion}
%{_prefix}/share/orthanc/plugins/*.so

%dir %{_sysconfdir}/orthanc
%config(noreplace) %{_sysconfdir}/orthanc/*.json
%dir %attr(0755, orthanc, orthanc) %{_sharedstatedir}/orthanc
%dir %attr(0755, orthanc, orthanc) %{_sharedstatedir}/orthanc/db-v6

%files -n orthanc-devel
%{_includedir}/*

%files -n orthanc-doc
%{_docdir}/orthanc/*



# Installation of the Systemd Orthanc service
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
%post
%systemd_post orthanc.service

%preun
%systemd_preun orthanc.service

%postun
%systemd_postun_with_restart orthanc.service


%pre
# http://fedoraproject.org/wiki/Packaging%3aUsersAndGroups
# "We never remove users or groups created by packages"

getent group orthanc >/dev/null || groupadd -r orthanc
getent passwd orthanc >/dev/null || \
    useradd -r -g orthanc -G orthanc -d %{_sharedstatedir}/orthanc -s /sbin/nologin \
    -c "User account that holds information for Orthanc" orthanc
exit 0


%changelog
* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.5.4-7
- Rebuild (jsoncpp)

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.5.4-6
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.4-4
- Rebuild (jsoncpp)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.4-2
- Rebuild (jsoncpp)

* Tue Feb 12 2019 Sebastien Jodogne <s.jodogne@gmail.com> - 1.5.4-1
- New upstream version
- Fix FTBFS (#1675600)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Sebastien Jodogne <s.jodogne@gmail.com> - 1.4.2-1
- New upstream version
- Fix ambiguous Python shebang

* Sat Jul 14 2018 Sebastien Jodogne <s.jodogne@gmail.com> - 1.4.0-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May  4 2018 Sebastien Jodogne <s.jodogne@gmail.com> - 1.3.2-1
- New upstream version
- Fix outdated dependencies in orthanc package (#1567513)

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0-6
- tcpwrappers has been retired

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 1.3.0-4
- Rebuilt for dcmtk

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.3.0-3
- Rebuilt for jsoncpp.so.20

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.3.0-2
- Rebuilt for jsoncpp-1.8.3

* Fri Aug 25 2017 Sebastien Jodogne <s.jodogne@gmail.com> - 1.3.0-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-5
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-3
- Rebuilt for Boost 1.63

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 1.1.0-2
- Rebuilt for libjsoncpp.so.11

* Tue Jun 28 2016 Sebastien Jodogne <s.jodogne@gmail.com> - 1.1.0-1
- New upstream version

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-3
- Rebuilt for linker errors in boost (#1331983)

* Mon Apr 11 2016 Sebastien Jodogne <s.jodogne@gmail.com> - 1.0.0-2
- Compatibility with CMake >= 3.5.0

* Fri Apr 08 2016 Sebastien Jodogne <s.jodogne@gmail.com> - 1.0.0-1
- New upstream version
- Add of "orthanc-devel" and "orthanc-doc"
- Removal of "orthancclient-lib/devel/doc" (now a separate project)

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 0.8.6-8
- Rebuilt for libjsoncpp.so.1
- Add Patch2, properly define system include dirs within CMake
- Add explicit BuildRequires libjpeg-devel libxml2-devel tcp_wrappers-devel

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.8.6-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.8.6-4
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 8 2015 Mario Ceresa <mrceresa@gmail.com> - 0.8.6-1
- New upstrean version

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.8.5-3
- Rebuild for boost 1.57.0

* Tue Dec 16 2014 Mario Ceresa <mrceresa@gmail.com> - 0.8.5-2
- Rebuild for dcmtk update

* Tue Nov  4 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.8.5-1
- New upstream version

* Fri Sep 12 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.8.3-1
- New upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.8.0-1
- New upstream version

* Thu Jun 12 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.7.6-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.7.5-2
- Rebuild for boost 1.55.0

* Fri May  9 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.7.5-1
- New upstream version

* Fri Feb 14 2014 Sebastien Jodogne <s.jodogne@gmail.com> - 0.7.3-1
- New upstream version

* Fri Nov  8 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.7.2-1
- New upstream version

* Wed Oct 30 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.7.1-1
- New upstream version
- Fix for big endian architectures (bug #985748)
- Packaging of the Orthanc Client library

* Mon Sep 16 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.6.1-1
- New upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.6.0-2
- Rebuild for boost 1.54.0

* Tue Jul 16 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.6.0-1
- New upstream version

* Wed May  8 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.5.2-1
- New upstream version

* Wed Apr 17 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.5.1-1
- New upstream version

* Thu Apr 04 2013 Sebastien Jodogne <s.jodogne@gmail.com> - 0.5.0-1
- New upstream version

* Wed Dec 19 2012 Sebastien Jodogne <s.jodogne@gmail.com> - 0.4.0-5
- Fixes according to reviews

* Wed Dec 19 2012 Sebastien Jodogne <s.jodogne@gmail.com> - 0.4.0-4
- Dynamic linking against mongoose-lib

* Wed Dec 19 2012 Sebastien Jodogne <s.jodogne@gmail.com> - 0.4.0-3
- Improvements to the packaging

* Tue Dec 18 2012 Sebastien Jodogne <s.jodogne@gmail.com> - 0.4.0-2
- Improvements to the packaging

* Mon Dec 17 2012 Sebastien Jodogne <s.jodogne@gmail.com> - 0.4.0-1
- Initial RPM Release