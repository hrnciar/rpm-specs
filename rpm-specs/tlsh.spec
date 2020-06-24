Name:           tlsh
Version:        3.17.0
Release:        4%{?dist}
Summary:        Fuzzy text matching library

License:        ASL 2.0
URL:            https://github.com/trendmicro/tlsh
Source0:        https://github.com/trendmicro/tlsh/archive/%{version}/tlsh-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%global _description %{expand:
TLSH is a fuzzy matching library. Given a byte stream with a minimum
length of 256 bytes (and a minimum amount of randomness), TLSH
generates a hash value which can be used for similarity comparisons.
Similar objects will have similar hash values which allows for the
detection of similar objects by comparing their hash values.}

%description %_description

%package doc
Summary: Documentation for TLSH
BuildArch: noarch

%description doc
%{summary}.

%package -n python3-tlsh
Summary:        Python 3 interface for TLSH
%{?python_provide:%python_provide python3-tlsh}
Obsoletes: tlsh < 3.17.0
Obsoletes: tlsh-devel < 3.17.0

%description -n python3-tlsh %_description

This package contains the %{summary}.

%prep
%autosetup
# I'm just loving cmake more every day
echo 'set(CMAKE_CXX_FLAGS "%{optflags} -fPIC")' | \
     tee -a src/CMakeLists.txt |\
     tee -a test/CMakeLists.txt |\
     tee -a utils/CMakeLists.txt

sed -r -i '/CMAKE_EXE_LINKER_FLAGS.*-static-libstdc/d' CMakeLists.txt

%build
mkdir build
pushd build
%cmake ..
popd
%make_build -C build
pushd py_ext
%py3_build
popd

%install
pushd py_ext
%py3_install
popd

%global _docdir_fmt %{name}

%check
bin/tlsh_version
bin/simple_unittest
# just check if we get 0 for identical files, and non-zero for different files
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/tlsh_unittest | grep -E '\b0\b'
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/simple_unittest | grep -vE '\b0\b'

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} \
        -c "import tlsh; print(tlsh.hash(open('LICENSE', 'rb').read()))"

%ldconfig_scriptlets

%files doc
%license LICENSE NOTICE.txt
%doc README.md
%doc TLSH_CTC_final.pdf
%doc TLSH_Introduction.pdf
%doc Attacking_LSH_and_Sim_Dig.pdf

%files -n python3-tlsh
%license LICENSE NOTICE.txt
%doc README.md
%{python3_sitearch}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.17.0-4
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.17.0-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.17.0-1
- Update to latest version (#1689880)
- Upstream doesn't provide a shared library anymore. The shared library made
  some sense when we had both python2- and python3- subpakcages. No other package
  in Fedora uses the shared library, and it seems that the ABI is not stable.
  This release drops the main binary package and the -devel subpackage and links
  the library statically into the python3 module.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-10
- Subpackage python2-tlsh has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar  9 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.4.5-1
- Initial version
