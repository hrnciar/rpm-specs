%global testspec_version 3.6.3
%if 0%{?epel} && 0%{?epel} <= 7
%define with_tests 0
%else
%define with_tests 0
%endif

Name:           sassc
Version:        3.6.1
Release:        6%{?dist}
Summary:        Wrapper around libsass to compile CSS stylesheet

License:        MIT
URL:            http://github.com/sass/sassc
Source0:        https://github.com/sass/sassc/archive/%{version}/%{name}-%{version}.tar.gz
# Test suite spec. According to this comment from an upstream dev, we should
# not use the release tags on the test spec:
# https://github.com/sass/libsass/issues/2258#issuecomment-268196004
# https://github.com/sass/sass-spec/archive/master.zip
# https://github.com/sass/sass-spec/archive/v%%{testspec_version}.tar.gz
Source1:        sass-spec-libsass-%{testspec_version}.tar.gz

# libsass is built as a shared library.
Patch0:         %{name}-3.5.0-build.patch

BuildRequires:  libsass-devel >= %{version}
BuildRequires:  gcc-c++
%if %{with_tests}
# For the test suite
BuildRequires:  ruby
%if 0%{?epel} && 0%{?epel} <= 7
BuildRequires:  rubygem-minitest5
%else
BuildRequires:  rubygem-hrx
BuildRequires:  rubygem-minitest
%endif
%endif

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.


%prep
%setup -q -a 1
mv sass-spec-libsass-%{testspec_version} sass-spec
%patch0 -p1


%build
%make_build build-shared \
    LDFLAGS="$RPM_OPT_FLAGS" \
    CFLAGS="$RPM_OPT_FLAGS" \
    CXXFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
install -p -m755 -D bin/sassc $RPM_BUILD_ROOT%{_bindir}/%{name}

%if %{with_tests}
%check
ruby sass-spec/sass-spec.rb  --impl libsass -c bin/%{name}
%endif

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}


%changelog
* Mon Aug 03 17:34:20 GMT 2020 Leigh Scott <leigh123linux@gmail.com> - 3.6.1-6
- Disable tests

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.6.1-2
- Add build requires rubygem-hrx and enable tests for fedora

* Mon Dec 02 2019 Leigh Scott <leigh123linux@gmail.com> - 3.6.1-1
- Upgrade to 3.6.1, tests 3.6.3
- Disable tests they fail due to missing rubygem-hrx

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 3.5.0-1
- Upgrade to 3.5.0, tests 3.5.4. 
- Fixes FTBFS.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Aurelien Bompard <abompard@fedoraproject.org> - 3.4.5-2
- Require the same libsass version

* Mon Jul 24 2017 Aurelien Bompard <abompard@fedoraproject.org> - 3.4.5-1
- Version 3.4.5: https://github.com/sass/sassc/releases/tag/3.4.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Aurelien Bompard <abompard@fedoraproject.org> - 3.4.1-1
- Version 3.4.1: https://github.com/sass/sassc/releases/tag/3.4.1

* Mon Dec 12 2016 Aurelien Bompard <abompard@fedoraproject.org> - 3.4.0-1
- Version 3.4.0: https://github.com/sass/sassc/releases/tag/3.4.0

* Tue Aug 23 2016 Aurelien Bompard <abompard@fedoraproject.org> - 3.3.6-1
- initial package
