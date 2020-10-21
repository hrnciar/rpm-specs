# Add generation of HMAC checksums of the final stripped binaries.
# %%define with lazy expansion is used here intentionally, because
# this needs to be expanded inside of a higher level macro that
# gets expanded itself.
%define __spec_install_post                    \
%{?__debug_package:%{__debug_install_post}}    \
%{__arch_install_post}                         \
%{__os_install_post}                           \
fipshmac %{buildroot}%{_bindir}/%{name}        \\\
  %{buildroot}%{_libexecdir}/%{name}           \\\
  %{buildroot}%{_datadir}/%{name}/config.json  \\\
  %{buildroot}%{_datadir}/%{name}/openssl.cnf  \
%{nil}

# Always do out-of-source builds with CMake.
%{?__cmake_in_source_build:%undefine __cmake_in_source_build}

# Build and package Doxygen documentation?
%bcond_without    doxy

# Package summary.  Gets overwritten by subpackages otherwise.
%global pkg_sum   Online identification with German ID card (Personalausweis)


Name:             AusweisApp2
Version:          1.20.2
Release:          9%{?dist}
Summary:          %{pkg_sum}

# Init forge packaging helpers.
%global forgeurl  https://github.com/Governikus/%{name}
%global tag       %{version}
%forgemeta

License:          EUPL 1.2
URL:              https://www.ausweisapp.bund.de/en
Source0000:       %{forgesource}
Source0001:       https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%%20EN.txt#/EUPL-12_EN.txt
Source0002:       gen_openssl_cnf.py

# Upstreamed.
Patch00001:       %{forgeurl}/pull/28.patch#/%{name}-1.20.1-doxygen_exclude_build_dir.patch

# Downstream.
Patch01000:       %{name}-1.20.1-use_Qt_TranslationsPath.patch

BuildRequires:    cmake
BuildRequires:    crypto-policies
BuildRequires:    desktop-file-utils
BuildRequires:    fipscheck
BuildRequires:    gcc-c++
BuildRequires:    help2man
BuildRequires:    http-parser-devel
BuildRequires:    java-openjdk-headless
BuildRequires:    libappstream-glib
BuildRequires:    libudev-devel
BuildRequires:    ninja-build
BuildRequires:    openssl-devel
BuildRequires:    pcsc-lite-devel
BuildRequires:    python3-devel
BuildRequires:    qt5-linguist
BuildRequires:    qt5-qtbase-devel
BuildRequires:    qt5-qtconnectivity-devel
BuildRequires:    qt5-qtdeclarative-devel
BuildRequires:    qt5-qtquickcontrols2-devel
BuildRequires:    qt5-qtsvg-devel
BuildRequires:    qt5-qtwebsockets-devel

# Lowercase package name.
%global lc_name   %{lua:print(string.lower(rpm.expand("%{name}")))}

# Make sure this package automatically replaces the security hazard
# built in some COPR.
Obsoletes:        %{name}            < 1.20.1
Obsoletes:        %{lc_name}         < 1.20.1

# Provide the lowercase name for convenience as well.
Provides:         %{lc_name}         = %{version}-%{release}
Provides:         %{lc_name}%{?_isa} = %{version}-%{release}

# Do not raise conflicts about shared license files.
Requires:         %{name}-data       = %{version}-%{release}
Requires:         (%{name}-doc       = %{version}-%{release} if %{name}-doc)

# Needed for running fipscheck on application startup.
# Requires:         fipscheck

%description
The AusweisApp2 is a software to identify yourself online
with your ID card (Personalausweis) or your electronic
residence permit (Aufenthalts- / Niederlassungserlaubis).

The AusweisApp2 also offers you an integrated self-assessment
in which you are able to view your data that is stored on the
online ID.


%package data
Summary:          Architecture-independent files used by %{name}
BuildArch:        noarch

Requires:         %{name}            = %{version}-%{release}
Requires:         hicolor-icon-theme

%description data
This package contains the architecture-independent files
used by %{name}.


%package doc
Summary:          User and API documentation for %{name}
BuildArch:        noarch

%if %{with doxy}
BuildRequires:    doxygen
BuildRequires:    graphviz
%endif
BuildRequires:    hardlink
BuildRequires:    python3-sphinx
BuildRequires:    python3-sphinx_rtd_theme

# Do not raise conflicts about shared license files.
Requires:         (%{name}           = %{version}-%{release} if %{name})

# The doc-api package is faded, since we can ship the
# Doxygen documentation noarch'ed as well now.
Obsoletes:        %{name}-doc-api    < 1.20.1-2
Provides:         %{name}-doc-api    = %{version}-%{release}

%description doc
This package contains the user and API documentation for %{name}.


%prep
%forgeautosetup -p 1
install -pm 0644 %{SOURCE1} LICENSE.en.txt

# Generate application specific OpenSSL configuration.
# See the comments in the resulting file for further information.
%{__python3} %{SOURCE2} resources/config.json.in \
  > fedora_%{name}_openssl.cnf

# Create the shell wrapper.
cat << EOF > fedora_%{name}_wrapper.sh
#!/bin/sh
# /usr/bin/fipscheck                               \\
#     %{_bindir}/%{name}                         \\
#     %{_libexecdir}/%{name}                     \\
#     %{_datadir}/%{name}/config.json           \\
#     %{_datadir}/%{name}/openssl.cnf           \\
# || exit \$?;
OPENSSL_CONF=%{_datadir}/%{name}/openssl.cnf  \\
%{_libexecdir}/%{name} "\$@";
EOF


%build
# The project does not ship any libraries that are meant to be
# consumed externally.  Thus we disable shared libs explicitly.
# See:  https://github.com/Governikus/AusweisApp2/pull/24
# and:  https://github.com/Governikus/AusweisApp2/pull/26
%cmake                                     \
  -DBUILD_SHARED_LIBS:BOOL=OFF             \
  -DBUILD_TESTING:BOOL=OFF                 \
  -DCMAKE_BUILD_TYPE:STRING=Release        \
  -DINTEGRATED_SDK:BOOL=OFF                \
  -DPYTHON_EXECUTABLE:STRING=%{__python3}  \
  -DSELFPACKER:BOOL=OFF                    \
  -G Ninja
%cmake_build

%if (0%{?fedora} || 0%{?rhel} > 8)
# Documentation.
%cmake_build --target inst inte notes sdk
%if %{with doxy}
%cmake_build --target doxy
%endif
%else
# Documentation.
%ninja_build -C %{_vpath_builddir} inst inte notes sdk
%if %{with doxy}
%ninja_build -C %{_vpath_builddir} doxy
%endif
%endif


%install
%cmake_install

# Relocate the application binary so we can call it through
# a shell wrapper and move installed files to proper locations.
mkdir -p %{buildroot}{%{_libexecdir},%{_qt5_translationdir}}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/translations/* \
  %{buildroot}%{_qt5_translationdir}
rm -fr %{buildroot}%{_datadir}/%{name}/translations

# Install the shell wrapper and custom OpenSSL configuration.
install -pm 0755 fedora_%{name}_wrapper.sh %{buildroot}%{_bindir}/%{name}
install -pm 0644 fedora_%{name}_openssl.cnf   \
  %{buildroot}%{_datadir}/%{name}/openssl.cnf

# Generate man-page.
mkdir -p %{buildroot}%{_mandir}/man1
help2man                                              \
  --no-discard-stderr --no-info                       \
  --manual="%{name}" --name="%{pkg_sum}" --section=1  \
  --help-option="--platform offscreen --help-all"     \
  --version-option="--platform offscreen --version"   \
  --output=%{buildroot}%{_mandir}/man1/%{name}.1      \
  %{buildroot}%{_libexecdir}/%{name}

# Excessive docs.
mkdir -p %{buildroot}%{_pkgdocdir}/{installation,integration,notes,sdk}
install -pm 0644 README.rst %{buildroot}%{_pkgdocdir}
%if %{with doxy}
mkdir -p %{buildroot}%{_pkgdocdir}/doxy
cp -a %{_vpath_builddir}/doc/html/* %{buildroot}%{_pkgdocdir}/doxy
%endif
cp -a %{_vpath_builddir}/docs/inst/html/* %{buildroot}%{_pkgdocdir}/installation
cp -a %{_vpath_builddir}/docs/inte/html/* %{buildroot}%{_pkgdocdir}/integration
cp -a %{_vpath_builddir}/docs/notes/html/* %{buildroot}%{_pkgdocdir}/notes
cp -a %{_vpath_builddir}/docs/sdk/html/* %{buildroot}%{_pkgdocdir}/sdk
find %{buildroot}%{_pkgdocdir} -type d -print0 | xargs -0 chmod -c 0755
find %{buildroot}%{_pkgdocdir} -type f -print0 | xargs -0 chmod -c 0644
find %{buildroot}%{_pkgdocdir} -type f -name '.*' -delete -print
hardlink -cfv %{buildroot}%{_pkgdocdir}

# Find installed icons.
find %{buildroot}%{_datadir}/icons/hicolor -type f -print | \
sed -e 's!^%{buildroot}!!g' > %{lc_name}.icons

# Find translation files.
%find_lang %{lc_name} --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.rst
%license AUTHORS
%license LICENSE.en.txt
%license LICENSE.txt
%{_bindir}/.%{name}.hmac
%{_bindir}/%{name}
%{_datadir}/applications/com.governikus.%{lc_name}.desktop
%{_libexecdir}/.%{name}.hmac
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/com.governikus.%{lc_name}.metainfo.xml


%files data -f %{lc_name}.icons -f %{lc_name}.lang
%{_datadir}/%{name}


%files doc
%doc %{_pkgdocdir}
%license %{_licensedir}/%{name}*


%changelog
* Sat Oct  3 12:51:03 CEST 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-9
- Disable fipscheck in shell wrapper as it does not work in Fedora 33+

* Sat Sep 26 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-8
- Make shell wrapper exit with the exit code of fipscheck on failure

* Sat Sep 26 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-7
- Calculate fipshmac for config files and shell wrapper
- Run fipscheck in shell wrapper before application starts

* Fri Sep 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-6
- Use a python script to generate a tailored OpenSSL configuration

* Thu Sep 24 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-5
- Some small spec file optimizations

* Thu Sep 24 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-4
- Use a more elaborate application specific OpenSSL configuration
  This also re-enables SHA384 hashes in ciphers

* Wed Sep 23 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-3
- Do not enable SHA384 ciphers in custom OpenSSL configuration

* Wed Sep 23 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-2
- Use application specific OpenSSL config through a shell wrapper

* Mon Sep 07 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.2-1
- New upstream release

* Mon Aug 24 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-3
- Add a patch to load translations from Qt5 TranslationsPath
- Move translation files to proper location
- Drop invokation of ctest, as we cannot run the testsuite
  from a release build
- Replace patch adding English license with the actual license file

* Fri Aug 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-2
- Add a patch to exclude the build directory in the Doxyfile
- Merge doc-api package with the doc package, since the Doxygen
  API documentation can be shipped noarch'ed as well now

* Wed Aug 19 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-1
- Initial import (#1851205)

* Fri Jul 17 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.11
- Use %%cmake_{build,install} macros on newer distributions

* Sat Jul 04 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.10
- Add license text in English language

* Fri Jun 26 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.9
- Also obsolete package with %%{name} previous to this package version

* Fri Jun 26 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.8
- Ensure archful packages always require equal architecture

* Fri Jun 26 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.7
- Make sure permissions of the documentation files are correct
- Remove hidden files in documentation
- Drop 'LICENSE.officially.txt', as it only applies to binary copies,
  which are distributed on behalf of the federal government of Germany

* Thu Jun 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.6
- Use '--help-all' option when generating man-page
- Split build of Doxygen API docs from building user docs

* Thu Jun 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.5
- Add generated man-page

* Thu Jun 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.4
- Use a macro for lowercase package name

* Thu Jun 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.3
- Use ninja-build instead of GNU Make to speed up the build a bit

* Thu Jun 25 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.2
- Adaptions for building on EPEL

* Wed Jun 24 2020 Björn Esser <besser82@fedoraproject.org> - 1.20.1-0.1
- Initial spec file for review
