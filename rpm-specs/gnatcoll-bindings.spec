Name:           gnatcoll-bindings
Version:        2018
Release:        7%{?dist}
Summary:        The GNAT Components Collection – bindings
Summary(sv):    GNAT Components Collection – bindningar

License:        GPLv3+
# The source files are GPLv3+ and GPLv2+. These combine into GPLv3+ on the
# binary code.
URL:            https://github.com/AdaCore/gnatcoll-bindings
Source:         http://mirrors.cdn.adacore.com/art/5b0ce9cfc7a4475261f97ca5#/gnatcoll-bindings-gpl-2018-src.tar.gz
# The long hexadecimal number is what identifies the file on the server.
# Don't forget to update it!
# The latest known address of the download page is:
# https://www.adacore.com/download/more

BuildRequires:  gcc-gnat gprbuild fedora-gnat-project-common sed dos2unix
BuildRequires:  gnatcoll-core-devel = %{version}
# Although it's not explicitly stated, I guess it's best to keep all the parts
# of Gnatcoll on the same version number.
BuildRequires:  gmp-devel python3-devel readline-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

# Gnatcoll.Python is excluded because of undefined symbols. It can be built by
# passing "--with python" to RPMbuild.
%bcond_with python

%global common_description_en \
This is the bindings module of the GNAT Components Collection. It provides \
bindings to GMP, Iconv, %{?with_python:Python, }Readline and Syslog. \
%{!?with_python:The Python binding is excluded until it works with Python 3.}

%global common_description_sv \
Detta är bindningsmodulen i GNAT Components Collection. Den tillhandahåller \
bindningar till GMP, Iconv, %{?with_python:Python, }Readline och Syslog. \
%{!?with_python:Pythonbindningen är utelämnad tills den fungerar med Python 3.}

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package -n gnatcoll-gmp
Summary:        The GNAT Components Collection – GMP binding
Summary(sv):    GNAT Components Collection – GMP-bindning

%description -n gnatcoll-gmp
This is the GMP component of the GNAT Components Collection. It is an interface
to the GNU Multiple Precision (GMP) arithmetic library.

%description -n gnatcoll-gmp -l sv
Detta är GMP-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket GNU Multiple Precision (GMP) för godtyckligt precisa
beräkningar.


%package -n gnatcoll-iconv
Summary:        The GNAT Components Collection – Iconv binding
Summary(sv):    GNAT Components Collection – Iconvbindning

%description -n gnatcoll-iconv
This is the Iconv component of the GNAT Components Collection. It is an
interface to libiconv for conversion between character encodings.

%description -n gnatcoll-iconv -l sv
Detta är Iconv-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket Iconv för omvandling mellan teckenkodningar.


%if %{with python}
%package -n gnatcoll-python
Summary:        The GNAT Components Collection – Python binding
Summary(sv):    GNAT Components Collection – Pythonbindning

%description -n gnatcoll-python
This is the Python component of the GNAT Components Collection. It is an
interface to the Python interpreter.

%description -n gnatcoll-python -l sv
Detta är Python-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot pythontolken.
%endif


%package -n gnatcoll-readline
Summary:        The GNAT Components Collection – Readline binding
Summary(sv):    GNAT Components Collection – Readlinebindning

%description -n gnatcoll-readline
This is the Readline component of the GNAT Components Collection. It is an
interface to the Readline library for interactive input from the user.

%description -n gnatcoll-readline -l sv
Detta är Readline-komponenten i GNAT Components Collection. Den är ett
gränssnitt mot biblioteket Readline för interaktiv inmatning från användaren.


%package -n gnatcoll-syslog
Summary:        The GNAT Components Collection – Syslog binding
Summary(sv):    GNAT Components Collection – Syslogbindning

%description -n gnatcoll-syslog
This is the Syslog component of the GNAT Components Collection. It is an
interface to the system logger on Unix-like systems.

%description -n gnatcoll-syslog -l sv
Detta är Syslog-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot Unixlika operativsystems loggfunktion.


%package devel
Summary:        Development files for the GNAT Components Collection – bindings
Summary(sv):    Filer för programmering med GNAT Components Collection – bindningar
Requires:       gnatcoll-gmp%{?_isa} = %{version}-%{release}
Requires:       gnatcoll-iconv%{?_isa} = %{version}-%{release}
%if %{with python}
Requires:       gnatcoll-python%{?_isa} = %{version}-%{release}
%endif
Requires:       gnatcoll-readline%{?_isa} = %{version}-%{release}
Requires:       gnatcoll-syslog%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description devel %{common_description_en}

The gnatcoll-bindings-devel package contains source code and linking information
for developing applications that use the GNAT Components Collection bindings.

%description devel -l sv %{common_description_sv}

Paketet gnatcoll-bindings-devel innehåller källkod och länkningsinformation som
behövs för att utveckla program som använder GNAT Components Collections
bindningar.


%global set_env export GNATCOLL_VERSION=%{version} \
                export BUILD=PROD \
                export LIBRARY_TYPE=relocatable \
                export GNATCOLL_ICONV_OPT=@/dev/null \
                export GNATCOLL_PYTHON_CFLAGS=`python3-config --cflags` \
                export GNATCOLL_PYTHON_LIBS=`python3-config --ldflags`
# Iconv is not a separate library, but an empty GNATCOLL_ICONV_OPT doesn't
# prevent GPRbuild from using the default "-liconv", so it's set to a value
# that makes no difference.


%prep
%autosetup -n gnatcoll-bindings-gpl-%{version}-src

# Convert line breaks.
dos2unix --keepdate gmp/examples/gmp_examples.gpr


%build
%{set_env}
for subdir in gmp iconv %{?with_python:python} readline syslog ; do
    component=gnatcoll_${subdir}
    gprbuild -P ${subdir}/${component}.gpr %{GPRbuild_optflags}
done


%install
%{set_env}
for subdir in gmp iconv %{?with_python:python} readline syslog ; do
    component=gnatcoll_${subdir}
    gprinstall -P ${subdir}/${component}.gpr \
               --prefix=%{buildroot}%{_prefix} \
               --lib-subdir=%{buildroot}%{_libdir} \
               --ali-subdir=%{buildroot}%{_libdir}/${component} \
               --no-lib-link -m --create-missing-dirs
    ln --symbolic --force lib${component}.so.%{version} \
       %{buildroot}%{_libdir}/lib${component}.so

    # Make the generated usage project file architecture-independent.
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=/python_(cflags|libs)/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Delete the package Linker, which contains linker parameters that a
    #    shared library normally doesn't need, and can contain architecture-
    #    specific pathnames.
    # 4: Delete two unused variables with architecture- specific values from
    #    gnatcoll_python.gpr.
    # 5: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 6: Replace the value of Library_Dir with Directories.Libdir.
    # 7: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

# GPRinstall's manifest files are architecture-specific because they contain
# what seems to be checksums of architecture-specific files, so they must not
# be under _datadir. Their function is poorly documented, but they seem to be
# used when GPRinstall uninstalls packages. The manifest files are therefore
# irrelevant in this RPM package, so delete them.
rm --recursive --force %{buildroot}%{_GNAT_project_dir}/manifests

# These files may be of some value to developers:
for subdir in iconv readline syslog ; do
    mkdir --parents %{buildroot}%{_docdir}/gnatcoll/${subdir}
    cp --preserve=timestamps ${subdir}/README.md \
       %{buildroot}%{_docdir}/gnatcoll/${subdir}/
done

# Move the examples to their proper place.
mv %{buildroot}%{_datadir}/examples/gnatcoll %{buildroot}%{_docdir}/gnatcoll/examples

# Install the license with a single pathname that is shared by the subpackages.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 %{buildroot}%{_licensedir}/%{name}/


%check
%{_rpmconfigdir}/check-rpaths


%files -n gnatcoll-gmp
%{_libdir}/libgnatcoll_gmp.so.*
%license %{_licensedir}/%{name}

%files -n gnatcoll-iconv
%{_libdir}/libgnatcoll_iconv.so.*
%license %{_licensedir}/%{name}

%if %{with python}
%files -n gnatcoll-python
%{_libdir}/libgnatcoll_python.so.*
%license %{_licensedir}/%{name}
%endif

%files -n gnatcoll-readline
%{_libdir}/libgnatcoll_readline.so.*
%license %{_licensedir}/%{name}

%files -n gnatcoll-syslog
%{_libdir}/libgnatcoll_syslog.so.*
%license %{_licensedir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gnatcoll*
%{_GNAT_project_dir}/*
%{_docdir}/gnatcoll


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-3
- Tagged the license file as such.

* Fri Mar 29 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-2
- Added more macro usage, more comments and ownership of a directory.

* Sat Mar 16 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-1
- new package
