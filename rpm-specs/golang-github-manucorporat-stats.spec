# Generated by go2rpm
%bcond_without check

# https://github.com/manucorporat/stats
%global goipath         github.com/manucorporat/stats
%global commit          3ba42d56d227cf2a6086b63baba5e00669235853

%gometa

%global common_description %{expand:
Go Stats library.}

%global golicenses      LICENSE

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go Stats library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 15:33:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git3ba42d5
- Initial package
