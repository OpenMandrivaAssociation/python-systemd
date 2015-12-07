Summary:        Python interface to systemd
Name:           python-systemd
Version:        231
Release:        1
Group:          System/Kernel and hardware
License:        LGPLv2+
Url:            https://github.com/systemd/python-systemd/archive/v%{version}.tar.gz
Source0:        python-systemd-%{version}.tar.gz
BuildRequires:	pkgconfig(python2)
BuildRequires:  python-devel
BuildRequires:	pkgconfig(libsystemd-journal)
%description
Provides Python scripting interface to systemd


%prep
%setup -q -n %{name}-%{version}


%build
python setup.py build_ext -i

%install
python setup.py install --root=%{buildroot}


%files
%defattr(0644,root,root,0755)
%doc README.md LICENSE.txt NEWS
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/python_systemd-%{version}-py%{py_ver}.egg-info


