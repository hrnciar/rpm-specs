%global packname AsioHeaders
%global packver  1.12.2-1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.12.2.1
Release:          2%{?dist}
Summary:          Asio C++ Header Files

License:          Boost
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)

%description
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.


%package devel
Summary:          Asio C++ Header Files

# Newer than the version that's in Fedora.
# https://bugzilla.redhat.com/show_bug.cgi?id=1551800
Provides: bundled(asio) = 1.12.2

Requires: openssl-devel
Recommends: boost-devel

%description devel
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files devel
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%license %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include


%changelog
* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.12.2.1-2
- rebuild for R 4

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.2.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.1.1-1
- initial package for Fedora
