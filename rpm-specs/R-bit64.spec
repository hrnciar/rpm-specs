%global packname  bit64
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.7
Release:          10%{?dist}
Summary:          A S3 Class for Vectors of 64bit Integers

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_0.9-7.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-bit >= 1.1-12, R-utils, R-methods, R-stats
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bit >= 1.1.12
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-stats

%description
Package 'bit64' provides serializable S3 atomic 64bit (signed) integers. These
are useful for handling database keys and exact counting in +-2^63. WARNING: do
not use them as replacement for 32bit integers, integer64 are not supported for
subscripting by R-core and they have different semantics when combined with
double, e.g. integer64 + double => integer64. Class integer64 can be used in
vectors, matrices, arrays and data.frames. Methods are available for coercion
from and to logicals, integers, doubles, characters and factors as well as many
elementwise and summary functions. Many fast algorithmic operations such as
'match' and 'order' support interactive data exploration and manipulation and
optionally leverage caching.


%prep
%setup -q -c -n %{packname}

echo 'PKG_LIBS = -lm' >> %{packname}/src/Makevars

for file in %{packname}/inst/ANNOUNCEMENT-0.9-Details.txt; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# We don't need these files.
rm -r %{buildroot}%{rlibdir}/%{packname}/exec


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT-0.8.txt
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT-0.9.txt
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT-0.9-Details.txt
%doc %{rlibdir}/%{packname}/README_devel.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.9.7-10
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.7-8
- Fix tests on s390x

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.7-7
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.9.7-3
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.7-2
- Clean up some files

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.7-1
- initial package for Fedora
