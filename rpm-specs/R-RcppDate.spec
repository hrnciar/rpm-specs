%global packname RcppDate
%global packver  0.0.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          'date' C++ Header Library for Date and Time Functionality

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-Rcpp
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel

# This does not appear to be the same version as in Fedora, but I'm not sure
# what version exactly.
# https://github.com/eddelbuettel/rcppdate/issues/2
Provides:         bundled(date)

%description
'date' is a C++ header library offering extensive date and time
functionality for the C++11, C++14 and C++17 standards written by Howard
Hinnant and released under the MIT license. A slightly modified version has
been accepted (along with 'tz.h') as part of C++20. This package regroups
all header files from the upstream repository by Howard Hinnant so that
other R packages can use them in their C++ code. At present, few of the
types have explicit 'Rcpp' wrapper though these may be added as needed.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


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


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.1-2
- Rebuild to fix dist tag

* Sat Aug 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.1-1
- initial package for Fedora
