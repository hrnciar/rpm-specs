Name:           gnatcoll
Version:        2018
Release:        6%{?dist}
Summary:        The GNAT Components Collection
Summary(sv):    GNAT Components Collection

License:        GPLv3+
# The source files are GPLv3+ and GPLv2+, except that getRSS.c is CC-BY. These
# combine into GPLv3+ on the binary code.
URL:            https://github.com/AdaCore/gnatcoll-core
Source:         http://mirrors.cdn.adacore.com/art/5b0819dfc7a447df26c27a99#/gnatcoll-core-gpl-2018-src.tar.gz
# The long hexadecimal number is what identifies the file on the server.
# Don't forget to update it!
# The latest known address of the download page is:
# https://www.adacore.com/download/more

# Backported adaptation to a compiler change:
# https://github.com/AdaCore/gnatcoll-core/commit/87cd0beb5c60676f6abeff89142f3909f3c2f04c
Patch1:         gnatcoll-2018-access_conversion.patch

BuildRequires:  gcc-gnat gprbuild make sed fedora-gnat-project-common
BuildRequires:  libgpr-devel >= 2018
BuildRequires:  xmlada-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

# The package "gnatcoll" is a metapackage that pulls in all the binary library
# packages to prevent problems when Fedora is upgraded:
Requires:       gnatcoll-core gnatcoll-gmp gnatcoll-iconv
Requires:       gnatcoll-readline gnatcoll-syslog
Requires:       gnatcoll-sql gnatcoll-sqlite gnatcoll-postgres gnatcoll-xref
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%global common_description_en \
The GNAT Components Collection is a library of general-purpose packages that \
are part of the GNAT technology. The components complement the predefined Ada \
and GNAT libraries and deal with a range of common programming issues \
including string and text processing, memory management, and file handling.

%global common_description_sv \
GNAT Components Collection är ett bibliotek med universalpaket som ingår i \
GNAT-sviten. Komponenterna kompletterar adas och GNATs fördefinierade \
bibliotek, och löser diverse vanliga programmeringsproblem såsom sträng- och \
textbehandling, minneshantering och filhantering.

%description %{common_description_en}

Gnatcoll has been divided into separate modules. The gnatcoll package pulls in
the binaries of all the modules to prevent problems when Fedora is upgraded.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description -l sv %{common_description_sv}

Gnatcoll har delats upp i skilda moduler. Paketet gnatcoll drar in alla
modulernas binärfiler för att undvika problem när Fedora uppgraderas.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.


%package devel
Summary:        Development metapackage for the GNAT Components Collection
Summary(sv):    Metapaket för programmering med GNAT Components Collection
Requires:       gnatcoll-core-devel gnatcoll-bindings-devel gnatcoll-db-devel
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%description devel %{common_description_en}

Gnatcoll has been divided into separate modules. The gnatcoll-devel package
pulls in the development packages of all the modules to prevent problems when
Fedora is upgraded.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv %{common_description_sv}

Gnatcoll har delats upp i skilda moduler. Paketet gnatcoll-devel drar in alla
modulernas programmeringspaket för att undvika problem när Fedora uppgraderas.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.


%package core
Summary:        The GNAT Components Collection – core packages
Summary(sv):    GNAT Components Collection – centrala paket

%description core %{common_description_en}

The gnatcoll-core package contains the core module of the GNAT Components
Collection.

%description core -l sv %{common_description_sv}

Paketet gnatcoll-core innehåller den centrala modulen i GNAT Components
Collection.


%package core-devel
Summary:        Development files for the GNAT Components Collection – core packages
Summary(sv):    Filer för programmering med GNAT Components Collection – centrala paket
Requires:       gnatcoll-core%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common libgpr-devel xmlada-devel
Recommends:     gnatcoll-doc
Suggests:       gnatcoll-bindings-devel gnatcoll-db-devel

%description core-devel %{common_description_en}

The gnatcoll-core-devel package contains source code and linking information for
developing applications that use the GNAT Components Collection core packages.

%description core-devel -l sv %{common_description_sv}

Paketet gnatcoll-core-devel innehåller källkod och länkningsinformation som
behövs för att utveckla program som använder GNAT Components Collections
centrala paket.


%package doc
Summary:        Documentation for the GNAT Components Collection – core packages
Summary(sv):    Dokumentation till GNAT Components Collection – centrala paket
BuildArch:      noarch
License:        MIT and BSD
# The documents have an MIT-like license. Some Javascript and CSS files that
# Sphinx includes with the documentation are BSD- and MIT-licensed.

%description doc %{common_description_en}

The gnatcoll-doc package contains the documentation for the GNAT Components
Collection.

%description doc -l sv %{common_description_sv}

Paketet gnatcoll-doc innehåller dokumentationen till GNAT Components Collection.


%prep
%autosetup -n gnatcoll-core-gpl-%{version}-src -p0


%build
make build-relocatable 'GPRBUILD_OPTIONS=%{GPRbuild_optflags}'


%install
make install-relocatable \
     'prefix=%{buildroot}%{_prefix} \
      --lib-subdir=%{buildroot}%{_libdir} \
      --ali-subdir=%{buildroot}%{_libdir}/%{name} \
      --no-lib-link'
# The makefile doesn't anticipate the need to pass additional parameters to
# GPRinstall, but it's possible to include them with the prefix and have them
# expanded as separate parameters.
# GPRinstall's -m option is defective. It removes too much filename data from
# the project file and misses some source files that need to be installed. To
# work around this -m is omitted, so even unnecessary sources are installed.

# These files aren't needed in the package.
rm %{buildroot}%{_pkgdocdir}/html/html/{.buildinfo,objects.inv}

# Fix up some things that Adacore does wrong.
ln --symbolic --force libgnatcoll.so.%{version} %{buildroot}%{_libdir}/libgnatcoll.so
mv %{buildroot}%{_datadir}/examples/gnatcoll %{buildroot}%{_pkgdocdir}/examples
mv %{buildroot}%{_pkgdocdir}/html/html/* %{buildroot}%{_pkgdocdir}/html/
rmdir %{buildroot}%{_pkgdocdir}/html/html

# GPRinstall's manifest files are architecture-specific because they contain
# what seems to be checksums of architecture-specific files, so they must not
# be under _datadir. Their function is poorly documented, but they seem to be
# used when GPRinstall uninstalls packages. The manifest file is therefore
# irrelevant in this RPM package, so delete it.
rm --recursive --force %{buildroot}%{_GNAT_project_dir}/manifests

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


%check
%{_rpmconfigdir}/check-rpaths


%files
# empty metapackage

%files devel
# empty metapackage

%files core
%license COPYING3
%{_libdir}/lib%{name}*.so.%{version}

%files core-devel
%{_GNAT_project_dir}/%{name}*
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libdir}/lib%{name}*.so

%files doc
%{_pkgdocdir}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2018-4
- Adapted to a change in GCC 10.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-2
- Worked around a bug in GPRinstall.

* Thu Mar 14 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-1
- Upgraded to gnatcoll-core 2018.
- This is now the gnatcoll-core source package. gnatcoll-bindings and gnatcoll-
  db are separate source packages.

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017-16
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-13
- Disable python3 support
- Change shebang to python3 (#1453185)

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-11
- rebuilt

* Fri Jan 05 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-10
- gnatcoll-devel requres libgpr-devel

* Fri Dec  1 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-9
- Build with new sources ( [QB29-004] )

* Fri Aug 04 2017  Pavel Zhukov <landgraf@fedoraproject.org> - 2017-7
- Enable gtkada

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-4
- Drop devel suffix
- New version (2017)

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 2016-5.1d
- Rebuild with new gprbuild

* Fri Jul  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 2016-4.1d
- Rebuild with new gnat

* Tue May 23 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2016-3
- Switch to python3 (#1453185)

* Sun Apr 16 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2016-2
- Disable gtkada in rawhide

* Sat Apr 15 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2016-1
- New version (#2016)

* Mon Aug 08 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2014-7
- Rebuilt to link to GTKada 3.14.2.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2014-6
- Rebuilt with GCC 6 prerelease.

* Mon Sep 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2014-5
- Rebuild (GtkAda3)
- Add docs to devel
- use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2014-3
- Enable GtkAda support

* Tue May 26 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2014-2
- New release (2014)
- Disabled Gtkada support
- Depends on gprbuild >= 2014

* Fri May 01 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2013-11
- Patched to build with GCC 5.

* Tue Mar 31 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-10
- Fix library dir

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-9
- Do not build on arm 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-6
- Use GNAT_arches rather than an explicit list

* Wed May  7 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-5
- Rebuild with new libgnat

* Wed Nov 20 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-4
- Fix parallel build in rawhide

* Tue Nov 19 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-2
- Add psql and sqlite to devel's requirement

* Sat Nov 02 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-1
- New release 2013 (1.6w)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 26 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 2012-7
- Rebuild with new libgmat
- Add gcc-gnat to BR

* Tue Jul 24 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2012-5
- Delete rpath from libraries
- Add lgpr files to project

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2012-3
- Update to 2012
- Fix library type in gpr
- Fix project files path

* Sat Mar 10 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2011-8
- Rebuild for new gprbuild 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-6
- Rebuild for new spm 

* Thu Aug 18 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-5
- Fix gnat_optflags

* Wed Aug 17 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-4
- Initial build
- Remove trailing @ from Makefile
- Add ifarch for rm
- Add ExcludeArch

