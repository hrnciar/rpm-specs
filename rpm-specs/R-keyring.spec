%global packname keyring
%global packver  1.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Access the System Credential Store from R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat, R-getPass, R-openssl, R-R6, R-utils, R-sodium, R-yaml, R-filelock, R-rappdirs, R-tools
# Suggests:  R-callr, R-covr, R-mockery, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-getPass
BuildRequires:    R-openssl
BuildRequires:    R-R6
BuildRequires:    R-utils
BuildRequires:    R-sodium
BuildRequires:    R-yaml
BuildRequires:    R-filelock
BuildRequires:    R-rappdirs
BuildRequires:    R-tools
BuildRequires:    R-callr
BuildRequires:    R-mockery
BuildRequires:    R-testthat
BuildRequires:    R-withr
BuildRequires:    pkgconfig(libsecret-1)

%description
Platform independent API to access the operating system's credential store.
Currently supports: Keychain on macOS, Credential Store on Windows, the Secret
Service API on Linux, and a simple, platform independent store implemented with
environment variables. Additional storage back-ends can be added easily.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


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
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/development-notes.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jun 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
