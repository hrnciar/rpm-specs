# Generated by go2rpm
%bcond_without check

# https://github.com/jung-kurt/gofpdf
%global goipath         github.com/jung-kurt/gofpdf
Version:                2.17.2

%gometa

%global common_description %{expand:
Package Gofpdf implements a PDF document generator with high level support for
text, drawing and images.}

%global golicenses      LICENSE
%global godocs          doc README.md document.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        PDF document generator with high level support for text, drawing and images

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in makefont; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jul 28 16:22:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.17.2-1
- Update to 2.17.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 00:00:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.7.1-1
- Initial package
